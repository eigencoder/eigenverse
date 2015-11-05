import logging
import json

from board import Board

logger = logging.getLogger(__name__)


class Game(object):
    def __init__(self, players, game_id=None, size=(10, 10), star_count=10):
        if game_id:
            logger.info("Loading game {id}".format(id=game_id))
            raise NotImplementedError
        self.id = 1
        self.players = players
        self.board = Board(bounds=size, star_count=star_count)

        logger.info("Game was init")

    def __repr__(self):
        return str(self.serialized)

    @property
    def serialized(self):
        return {'game_id': self.id,
                'players': self.players,
                'board': self.board,
               }
