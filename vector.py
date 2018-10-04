import unittest


class Vector():
    def __init__(self, coordinates):
        if not coordinates:
            raise ValueError("Coordinates is required.")

        self.coordinates = tuple(coordinates)
        self.dimension = len(coordinates)

    def __add__(self, other):
        if self.dimension != other.dimension:
            raise ValueError("Cannot add vectors with different dimensions.")

        return Vector([a+b for a, b in zip(self.coordinates, other.coordinates)])

    def __str__(self):
        return "Vector: {}".format(self.coordinates)

    def __eq__(self, other):
        return self.coordinates == other.coordinates

class VectorTest(unittest.TestCase):
    """
    Test Vector class.
    """
    def testAdd2Vectors(self):
        v1 = Vector([1, 2, 3])
        v2 = Vector([4, 2, -6])

        v = Vector([5, 4, -3])
        self.assertEqual(v, v1 + v2)

    def testAddMultipleVectors(self):
        v1 = Vector([1, 2, 3])
        v2 = Vector([4, 2, -6])
        v3 = Vector([-2, 3, 1])

        v = Vector([3, 7, -2])
        self.assertEqual(v, v1 + v2 + v3)

    def testAddZeroVector(self):
        v0 = Vector([0, 0, 0])
        v1 = Vector([1, 2, 3])

        self.assertEqual(v1, v1 + v0)

    def testAddOppositeVectors(self):
        v1 = Vector([1, 2, 3])
        v2 = Vector([-1, -2, -3])

        v = Vector([0, 0, 0])
        self.assertEqual(v, v1 + v2)

if __name__ == '__main__':
    unittest.main()
