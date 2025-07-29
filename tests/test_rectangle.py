import pytest
from rectangle import Rectangle

@pytest.fixture
def rectangle():
    return Rectangle(3, 4)

def test_area(rectangle):
    assert rectangle.area() == 12

def test_area2(rectangle):
    assert rectangle.area() == 1
