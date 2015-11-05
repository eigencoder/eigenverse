import unittest
from ..src.star import Star


class TestStar(unittest.TestCase):

    def test_in_bounds(self):
        star = Star(bounds=(10, 10))
        self.assertTrue(star.x >= 0, "Star's x location is not as expected: {x}".format(x=star.x))
        self.assertTrue(star.x <= 10, "Star's x location is not as expected: {x}".format(x=star.x))

    def test_coordinates(self):
        star = Star(coordinates=[3, 5])  # Coordinates can be a tuple or list
        self.assertEqual(star.x, 3, "Star's x location is not as expected: {x}".format(x=star.x))
        self.assertEqual(star.y, 5, "Star's y location is not as expected: {y}".format(y=star.y))
        self.assertEqual(star.z, 0, "Star's z location should default to 0. Got {z}".format(z=star.z))

    def test_loc_4d(self):
        star = Star(coordinates=(3, 4, 11, 13))
        self.assertEqual(star.x, 3, "Star's x location is not as expected: {x}".format(x=star.x))
        self.assertEqual(star.y, 4, "Star's y location is not as expected: {y}".format(y=star.y))
        self.assertEqual(star.z, 11, "Star's z location is not as expected: {loc}".format(loc=star.z))
        self.assertEqual(star[2], 11, "Star's 3rd dimension is not as expected: {loc}".format(loc=star[2]))
        self.assertEqual(star[3], 13, "Star's 4th dimension is not as expected: {loc}".format(loc=star[3]))

    def test_serialized_property(self):
        star = Star(coordinates=(3, 5))
        expected_dict = {'points_avail': 1, 'coordinates': (3, 5)}
        self.assertEqual(star.serialized['coordinates'], (3, 5), "Star coordinates failed")
        self.assertEqual(star.serialized['points_avail'], 1, "Star points available failed")
        # Overall test, will need to be updated as structure changes (and add above test)
        self.assertEqual(star.serialized, expected_dict, "Star serialization not as expected")

    def test_repr(self):
        # This should have all data required to recreate object. Update as necessary
        star = Star(coordinates=(3, 5))
        r = str(repr(star))
        expected_str = "{'points_avail': 1, 'coordinates': (3, 5)}"
        self.assertEqual(r, expected_str, "repr syntax or values not as expected")

if __name__ == '__main__':
    unittest.main()