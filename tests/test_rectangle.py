import pytest
from src.rectangle import Rectangle


@pytest.mark.parametrize('side_a, side_b, perimeter, area',
                         [
                             (1, 2, 6, 2)
                         ])
def test_rectangle(side_a, side_b, perimeter, area):
    s = Rectangle(side_a, side_b)
    assert s.name == 'Rectangle'
    assert s.perimeter() == perimeter
    assert s.area() == area


@pytest.mark.parametrize('side_a, side_b',
                         [
                             (1, 0),
                             (0, 0),
                             (-1, 1),
                             (-2, -3),
                             ('3', 1),
                             ('k', 'l')
                         ])
def test_rectangle_negative(side_a, side_b):
    with pytest.raises(ValueError):
        Rectangle(side_a, side_b)
