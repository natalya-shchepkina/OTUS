import pytest

from src.rectangle import Rectangle
from src.square import Square


@pytest.mark.parametrize('side_a, side_b, sum_areas',
                         [
                             (1, 2, 3)
                         ])
def test_add_area(side_a, side_b, sum_areas):
    r = Rectangle(side_a, side_b)
    s = Square(side_a)
    assert r.add_area(s) == sum_areas


@pytest.mark.parametrize('object_',
                         [
                             0,
                             True,
                             None,
                             10,
                             'str'
                         ])
def test_add_area_negative(object_):
    with pytest.raises(ValueError):
        r = Rectangle(1, 2)
        r.add_area(object_)
