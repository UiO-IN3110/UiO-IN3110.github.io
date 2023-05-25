from pkg.printing import print_red
from pkg.printing.printing import RED  # This deserves a comment


def test_print_red():
    result = print_red("BLUE")
    assert result == RED
