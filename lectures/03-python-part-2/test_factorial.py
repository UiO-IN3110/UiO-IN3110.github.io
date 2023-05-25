# Test of factorial function from module
import pytest
from factorial_doctest_exceptions import factorial


def test_correctness():
    assert factorial(0) == 1
    assert factorial(1) == 1


# We can generate more tests with decorators
@pytest.mark.parametrize("inp, out", [(2, 2), (3, 6)])
def test_correctness_dec(inp, out):
    assert factorial(inp) == out


def test_raises_not_int():
    with pytest.raises(AssertionError):
        factorial("1")


def test_raises_negative():
    with pytest.raises(ValueError):
        factorial(-1)


@pytest.mark.xfail
def test_expected_fail():
    assert factorial(3) == 4


def test_will_fail():
    assert factorial(5) == 6
