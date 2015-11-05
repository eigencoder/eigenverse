import unittest
from ..src.baseunit import BaseUnit


class TestBaseUnit(unittest.TestCase):

    def test_coordinates(self):
        b_unit = BaseUnit(coordinates=[3, 5])  # Coordinates can be a tuple or list
        self.assertEqual(b_unit.x, 3, "b_unit's x location is not as expected: {x}".format(x=b_unit.x))
        self.assertEqual(b_unit.y, 5, "b_unit's y location is not as expected: {y}".format(y=b_unit.y))
        self.assertEqual(b_unit.z, 0, "b_unit's z location should default to 0. Got {z}".format(z=b_unit.z))

    def test_loc_4d(self):
        b_unit = BaseUnit(coordinates=(3, 4, 11, 13))
        self.assertEqual(b_unit.x, 3, "b_unit's x location is not as expected: {x}".format(x=b_unit.x))
        self.assertEqual(b_unit.y, 4, "b_unit's y location is not as expected: {y}".format(y=b_unit.y))
        self.assertEqual(b_unit.z, 11, "b_unit's z location is not as expected: {loc}".format(loc=b_unit.z))
        self.assertEqual(b_unit[2], 11, "b_unit's 3rd dimension is not as expected: {loc}".format(loc=b_unit[2]))
        self.assertEqual(b_unit[3], 13, "b_unit's 4th dimension is not as expected: {loc}".format(loc=b_unit[3]))


    # Make a generic function to perform these tests. ie check_values({}) or check_defined(['dps', 'hp'])

    def test_serialized_property(self):
        b_unit = BaseUnit(coordinates=(3, 5))
        self.assertEqual(b_unit.serialized['coordinates'], (3, 5), "b_unit coordinates failed")
        self.assertEqual(b_unit.serialized['hp'], 1, "b_unit hp failed")
        self.assertEqual(b_unit.serialized['dps'], 0.1, "b_unit dps failed")

    #Probably don't need this. Serialized is enough
    def test_repr(self):
        # This should have all data required to recreate object. Update as necessary
        b_unit = BaseUnit(coordinates=(3, 5))
        r = str(repr(b_unit))
        self.assertTrue('coordinates' in r, "Collected_stars not found in repr")
        self.assertTrue('hp' in r, "Collected_stars not found in repr")
        self.assertTrue('dps' in r, "Collected_stars not found in repr")

if __name__ == '__main__':
    unittest.main()