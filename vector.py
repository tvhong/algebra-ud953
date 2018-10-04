import numbers
import unittest


class Vector():
    def __init__(self, coordinates):
        if not coordinates:
            raise ValueError("Coordinates is required.")

        self.coordinates = tuple(coordinates)
        self.dimension = len(coordinates)

    def __add__(self, other):
        return self._operate_on_other_vector(other, lambda a, b: a + b)

    def __sub__(self, other):
        return self._operate_on_other_vector(other, lambda a, b: a - b)

    def __mul__(self, other):
        if isinstance(other, numbers.Real):
            return Vector([other*x for x in self.coordinates])
        else:
            return self._operate_on_other_vector(other, lambda a, b: a * b)

    def _operate_on_other_vector(self, other, operator):
        """
        Helps run the simple Vector operators.
        :param operator: function that takes (a, b) and returns a result.
        """
        if self.dimension != other.dimension:
            raise ValueError("Cannot operate on vectors with different dimensions.")

        return Vector([operator(a, b) for a, b in zip(self.coordinates, other.coordinates)])

    def __str__(self):
        return "Vector: {}".format(self.coordinates)

    def __eq__(self, other):
        return self.coordinates == other.coordinates

    __radd__ = __add__
    __rmul__ = __mul__
    __repr__ = __str__


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

    def testSub2Vectors(self):
        v1 = Vector([1, 2, 3])
        v2 = Vector([3, 5, -4])

        v = Vector([-2, -3, 7])
        self.assertEqual(v, v1 - v2)

    def testSubMultipleVectors(self):
        v1 = Vector([1, 2, 3])
        v2 = Vector([3, 5, -4])
        v3 = Vector([0, 2, 2])

        v = Vector([-2, -5, 5])
        self.assertEqual(v, v1 - v2 - v3)

    def testSubZero(self):
        v0 = Vector([0, 0, 0])
        v1 = Vector([1, 2, 3])

        v = Vector([1, 2, 3])
        self.assertEqual(v, v1 - v0)

    def testSubSameVector(self):
        v1 = Vector([1, 2, 3])
        v2 = Vector([1, 2, 3])

        v = Vector([0, 0, 0])
        self.assertEqual(v, v1 - v2)

    def testMul2Vectors(self):
        v1 = Vector([1, 2, 3])
        v2 = Vector([3, 2, 1])

        v = Vector([3, 4, 3])
        self.assertEqual(v, v1 * v2)

    def testMulMultipleVectors(self):
        v1 = Vector([1, 2, 3])
        v2 = Vector([3, 2, 1])
        v3 = Vector([2, 2, 2])

        v = Vector([6, 8, 6])
        self.assertEqual(v, v1 * v2 * v3)

    def testMulWithIdentityVector(self):
        v1 = Vector([1, 2, 3])
        v2 = Vector([1, 1, 1])

        v = Vector([1, 2, 3])
        self.assertEqual(v, v1 * v2)

    def testMulWithZeroVector(self):
        v0 = Vector([0, 0, 0])
        v1 = Vector([1, 2, 3])

        self.assertEqual(v0, v1 * v0)

    def testMulWithARealNumber(self):
        v1 = Vector([1, 2, 3])
        coefficient = 1.111

        v = Vector([1.111, 2.222, 3.333])
        self.assertEqual(v, coefficient * v1)

    def testMulWithZero(self):
        v1 = Vector([1, 2, 3])
        coefficient = 0

        v = Vector([0, 0, 0])
        self.assertEqual(v, coefficient * v1)

    def testMulWithOne(self):
        v1 = Vector([1, 2, 3])
        coefficient = 1

        v = Vector([1, 2, 3])
        self.assertEqual(v, coefficient * v1)

    def testMulWithNegativeNumber(self):
        v1 = Vector([1, 2, 3])
        coefficient = -1

        v = Vector([-1, -2, -3])
        self.assertEqual(v, coefficient * v1)


if __name__ == '__main__':
    unittest.main()
