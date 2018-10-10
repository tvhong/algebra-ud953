import math
import unittest
from vector import Vector

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

    def testMagnitudeForZeroVector(self):
        v = Vector([0, 0, 0])
        self.assertEqual(0, v.magnitude)

    def testMagnitudeForSimple2DVector(self):
        v = Vector([1, 1])
        self.assertEqual(math.sqrt(2), v.magnitude)

    def testMagnitudeWithNegativeCoordinates(self):
        v = Vector([1, -1, -2])
        self.assertEqual(math.sqrt(6), v.magnitude)

    def testUnitWorks(self):
        v1 = Vector([2, -5, 3, 4])

        v = 1/v1.magnitude * v1
        self.assertEqual(v, v1.unit)

    def testUnitRaisesExeptionForZeroVector(self):
        v = Vector([0, 0, 0])
        with self.assertRaisesRegex(TypeError, '[Zz]ero'):
            v.unit

    def testUnitReturnsSameVectorForAUnitVector(self):
        v = Vector([1, 0, 0])
        self.assertEqual(v, v.unit)


if __name__ == '__main__':
    unittest.main()
