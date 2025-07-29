import pytest
from rectangle import Rectangle
from Square import Square

@pytest.fixture
def rectangle():
    return Rectangle(3, 4)

def square():
    return Square(3)

def test_area(rectangle):
    assert rectangle.area() == 12

def test_area_square(square):
    assert square.area() == 9
