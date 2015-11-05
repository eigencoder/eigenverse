import unittest
from ..src.player import Player


class TestPlayer(unittest.TestCase):

    # def test_in_bounds(self):
    #     player = Player(coordinates=(1,2))
    #     self.assertEqual(player.x, 1, "Player's x location is not as expected: {x}".format(x=player.x))
    #     self.assertEqual(player.y, 2, "Player's y location is not as expected: {y}".format(y=player.y))

    def test_serialized_property(self):
        player = Player()
        # self.assertEqual(player.serialized['coordinates'], (1, 2), "Player coordinates failed")
        self.assertEqual(player.serialized['collected_stars'], 0, "Player points collected failed")

    def test_repr(self):
        # This should have all data required to recreate object. Update as necessary
        player = Player()
        r = str(repr(player))
        # self.assertTrue('coordinates' in r, "Coordinates not found in repr")
        self.assertTrue('collected_stars' in r, "Collected_stars not found in repr")

    def test_move(self):
        pass

if __name__ == '__main__':
    unittest.main()