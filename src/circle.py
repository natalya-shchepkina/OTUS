from src.figure import Figure


class Circle(Figure):
    def __init__(self, radius: int | float):
        if not isinstance(radius, (int, float)) or radius <= 0:
            raise ValueError('Can not create Circle')
        self.name = 'Circle'
        self.radius = radius

    def area(self):
        return 2 * 3.14 * self.radius ** 2

    def circumference(self):
        return 2 * 3.14 * self.radius
