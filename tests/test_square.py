import pytest
from src.square import Square


@pytest.mark.parametrize('side_a, perimeter, area',
                         [
                             (2, 8, 4)
                         ])
def test_square(side_a, perimeter, area):
    s = Square(side_a)
    assert s.name == 'Square'
    assert s.perimeter() == perimeter
    assert s.area() == area


@pytest.mark.parametrize('side_a',
                         [
                             0,
                             -1,
                             'j'
                         ])
def test_square_negative(side_a):
    with pytest.raises(ValueError):
        Square(side_a)
