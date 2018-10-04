class Vector():
    def __init__(self, coordinates):
        if not coordinates:
            raise ValueError("Coordinates is required.")

        self.coordinates = coordinates
        self.dimension = len(coordinates)

    def __str__(self):
        return "Vector: {}".format(self.coordinates)

    def __eq__(self, other):
        return self.coordinates == other.coordinates
