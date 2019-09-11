from math_tools import absolute_value

def test_absolute_value():
    assert absolute_value(-3) == 3
    assert absolute_value(5) == 5
    assert absolute_value(0) == 0
