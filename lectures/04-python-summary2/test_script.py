from script import absolute_value

def test_func():
    assert absolute_value(-3) == 3
    assert absolute_value(5) == 5
    assert absolute_value(0) == 0
