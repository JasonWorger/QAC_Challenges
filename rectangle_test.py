import pytest
import rectangle

def test_rectangle_returns_correct_area():
    rect = rectangle.Rectangle(5,6)
    assert rect.area() == 30

