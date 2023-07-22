from abc import ABC, abstractmethod


class Figure(ABC):
    @abstractmethod
    def area(self):
        pass

    def add_area(self, other_figure):
        if isinstance(other_figure, Figure):
            return self.area() + other_figure.area()
        raise ValueError(f'Object {other_figure} is not Figure')
