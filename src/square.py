from src.rectangle import Rectangle


class Square(Rectangle):
    def __init__(self, side_a: int):
        if not isinstance(side_a, (int, float)) or side_a <= 0:
            raise ValueError('Can not create Square')
        super().__init__(side_a, side_a)
        self.name = 'Square'
        self.side_a = side_a
