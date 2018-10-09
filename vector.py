import math
import numbers

from decimal import Decimal


class Vector():
    """
    A class that represents Vectors.
    
    This should be treated as an immutable class.
    """

    def __init__(self, coordinates):
        if not coordinates:
            raise ValueError("Coordinates is required.")

        self.coordinates = tuple([Decimal(str(x)) for x in coordinates])
        self.dimension = len(coordinates)
        self.magnitude = math.sqrt(sum(x*x for x in self.coordinates))

    def __add__(self, other):
        return self._operate_on_other_vector(other, lambda a, b: a + b)

    def __sub__(self, other):
        return self._operate_on_other_vector(other, lambda a, b: a - b)

    def __mul__(self, other):
        if isinstance(other, numbers.Real):
            other = Decimal(str(other))
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
        return "Vector: {}".format([str(x) for x in self.coordinates])

    def __eq__(self, other):
        return self.coordinates == other.coordinates

    __radd__ = __add__
    __rmul__ = __mul__
    __repr__ = __str__
