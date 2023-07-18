import pytest
from src.circle import Circle


@pytest.mark.parametrize('radius, circumference, area',
                         [
                             (2, 12.56, 25.12)
                         ])
def test_circle(radius, circumference, area):
    c = Circle(radius)
    assert c.name == 'Circle'
    assert c.circumference() == circumference
    assert round(c.area(), 2) == area


@pytest.mark.parametrize('radius',
                         [
                             0,
                             -1,
                             'j'
                         ])
def test_circle_negative(radius):
    with pytest.raises(ValueError):
        Circle(radius)
