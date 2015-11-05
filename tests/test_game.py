import unittest
from ..src.game import Game


class TestGame(unittest.TestCase):

    def test_serialized(self):
        g = Game(players=['Player1', 'Player2'], size=(10, 10))
        data = g.serialized
        self.assertTrue(data['game_id'], "Game must have an ID")
        self.assertEqual(len(data['players']), 2, "Game must have exactly two players")

        from ..src.board import Board
        self.assertTrue(isinstance(data['board'], Board), "Game must have a board")

    def test_board(self):
        board_size = (7, 11)
        g = Game(players=['Player1', 'Player2'], size=board_size)
        self.assertEqual(g.board.size, board_size, "Board size must match size set on init")

    def test_stars(self):
        star_count = 10
        g = Game(players=['Player1', 'Player2'], size=(10, 10), star_count=star_count)
        stars = g.board.stars
        self.assertEqual(len(stars), star_count, "There should be exactly {count} stars".format(count=star_count))
