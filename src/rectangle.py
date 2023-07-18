from src.figure import Figure


class Rectangle(Figure):
    def __init__(self, side_a: int, side_b: int):
        if not isinstance(side_a, (int, float)) \
                or not isinstance(side_b, (int, float)) \
                or side_a <= 0 \
                or side_b <= 0:
            raise ValueError('Can not create Rectangle')
        self.name = 'Rectangle'
        self.side_a = side_a
        self.side_b = side_b

    def area(self):
        return self.side_a * self.side_b

    def perimeter(self):
        return 2 * (self.side_a + self.side_b)
