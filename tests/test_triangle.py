import pytest
from src.triangle import Triangle


@pytest.mark.parametrize('side_a, side_b, side_c, perimeter, area',
                         [
                             (5, 5, 6, 16, 12),
                             (3, 3, 4, 10, 4.472)
                         ])
def test_triangle(side_a, side_b, side_c, perimeter, area):
    t = Triangle(side_a, side_b, side_c)
    assert t.name == 'Triangle'
    assert t.perimeter() == perimeter
    assert round(t.area(), 3) == area


@pytest.mark.parametrize('side_a, side_b, side_c',
                         [
                             (1, 2, 3),
                             (0, 0, 0),
                             (-5, 5, 6),
                             (5, 0, 6),
                             (5, 5, 'j')

                         ])
def test_triangle_negative(side_a, side_b, side_c):
    with pytest.raises(ValueError):
        Triangle(side_a, side_b, side_c).area()
