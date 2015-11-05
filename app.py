import time
from threading import Thread
from flask import Flask, render_template, session
from flask.ext.socketio import SocketIO, emit, disconnect
from flask_debugtoolbar import DebugToolbarExtension

from src.game import Game

from gevent import monkey
monkey.patch_all()

app = Flask(__name__)
app.debug = True
app.config['SECRET_KEY'] = 'secret!'
app.debug = True
socketio = SocketIO(app)
thread = None
toolbar = DebugToolbarExtension(app)

GAMES = {}


def background_thread():
    """Example of how to send server generated events to clients."""
    count = 0
    while True:
        time.sleep(10)
        count += 1
        socketio.emit('my response',
                      {'data': 'Server generated event', 'count': count},
                      namespace='/api')


@socketio.on('newgame', namespace='/api')
def newgame(message):
    message['data'] = "Game started"
    game = Game(players=['player1', 'player2'])
    GAMES[game.id] = game
    # session['player_id'] = message.get('player_id')
    # session['game_id'] = 1
    session['receive_count'] = session.get('receive_count', 0) + 1
    emit('my response',
         {'data': str(game), 'count': session['receive_count']})



@app.route('/load')
def load():
    return render_template('index.html')


@app.route('/')
def index():
    global thread
    if thread is None:
        thread = Thread(target=background_thread)
        thread.start()
    return render_template('index.html')


@socketio.on('my event', namespace='/api')
def test_message(message):
    session['receive_count'] = session.get('receive_count', 0) + 1
    emit('my response',
         {'data': message['data'], 'count': session['receive_count']})


@socketio.on('my broadcast event', namespace='/api')
def test_broadcast_message(message):
    session['receive_count'] = session.get('receive_count', 0) + 1
    emit('my response',
         {'data': message['data'], 'count': session['receive_count']},
         broadcast=True)


@socketio.on('disconnect request', namespace='/api')
def disconnect_request():
    session['receive_count'] = session.get('receive_count', 0) + 1
    emit('my response',
         {'data': 'Disconnected!', 'count': session['receive_count']})
    disconnect()


@socketio.on('connect', namespace='/api')
def test_connect():
    print "User Connected"
    emit('my response', {'data': 'Connected', 'count': 0})


@socketio.on('disconnect', namespace='/api')
def test_disconnect():
    print('Client disconnected')


if __name__ == '__main__':
    socketio.run(app, port=5001)
