import unittest
from ..src.point import Point


class TestPoint(unittest.TestCase):
    def setUp(self):
        self.v1 = Point([1, 2, 3])
        self.v2 = Point([4, 5, 7])
        self.v3 = Point([4, ])

    def test_add(self):
        expected = Point([5, 7, 10])
        result = self.v1 + self.v2
        self.assertEqual(expected, result, "Point-wise summation failed")

    def test_sub(self):
        expected = Point([-3, -3, -4])
        result = self.v1 - self.v2
        self.assertEqual(expected, result, "Point-wise subtraction failed")

    def test_mul(self):
        expected = Point([4, 10, 21])
        result = self.v1 * self.v2
        self.assertEqual(expected, result, "Dot-product (multiplication) failed")

    def test_access(self):
        v2 = self.v2
        self.assertEqual(v2.x, 4)
        self.assertEqual(v2.y, 5)
        self.assertEqual(v2.z, 7)
        self.assertEqual(v2[0], 4)
        self.assertEqual(v2[-1], 7)

    def test_z_default(self):
        self.assertEqual(self.v3.z, 0)
        with self.assertRaises(IndexError):
            self.v3[2]  # This is not meant to work but could be changed if necessary

    def test_iter(self):
        self.assertEqual([x for x in self.v2], [4, 5, 7]), "Iteration should return all elements"

    def test_init(self):
        self.assertEqual(Point().x, 0)

    def test_dist(self):
        v1 = self.v1
        v2 = self.v2
        self.assertEqual(v1.dist(v2) ** 2, 34)
        self.assertEqual(v1.dist(v2), v2.dist(v1), "Distance (norm2) should be commutative")

    def test_not_equal(self):
        self.assertTrue(self.v1 != self.v2, "These two points should not be equal, and operation should be supported")
        self.assertFalse(self.v1 == self.v2, "These two points should not be equal, and operation should be supported")

    def test_size(self):
        self.assertEqual(self.v2.size, 3, "v2 should be a 3d point")

    def test_serialized(self):
        ser = self.v1.serialized
        expected = {'location': [1, 2, 3]}
        self.assertEqual(ser, expected, "Serialization or its structure failed")


if __name__ == '__main__':
    unittest.main()
