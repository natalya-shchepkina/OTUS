from src.figure import Figure
import math


class Triangle(Figure):
    def __init__(self, side_a: int | float, side_b: int | float, side_c: int | float):
        if not isinstance(side_a, (int, float)) \
                or not isinstance(side_b, (int, float)) \
                or not isinstance(side_c, (int, float)) \
                or side_a <= 0 or side_b <= 0 or side_c <= 0:
            raise ValueError('Can not create Triangle')
        self.name = 'Triangle'
        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c

    def perimeter(self):
        return self.side_a + self.side_b + self.side_c

    def area(self):
        semi_perimeter = self.perimeter() / 2
        area = math.sqrt(semi_perimeter
                         * (semi_perimeter - self.side_a)
                         * (semi_perimeter - self.side_b)
                         * (semi_perimeter - self.side_c))
        if area > 0:
            return area
        raise ValueError('Can not create Triangle')
