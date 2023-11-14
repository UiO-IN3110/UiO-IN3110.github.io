def factorial(n: int) -> int:
    """Return the factorial of n, an exact integer >= 0.

    Args:
       n (int):  n!

    Returns:
       int.  The factorial value::

    >>> factorial(5)
    120
    >>> factorial(0)
    1

    """
    if n == 0:
        return 1
    return n * factorial(n - 1)


if __name__ == "__main__":
    import math
    import sys

    N = int(sys.argv[1])
    print(f"Testing user defined factorial function for {N=}")
    user_n = factorial(N)
    ref_factorial = math.factorial(N)
    assert user_n == math.factorial(
        N
    ), f"Factorial function returning wrong answer {user_n}!={ref_factorial}"
