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


# --------------------------------------------------------------------

if __name__ == "__main__":
    import doctest

    doctest.testmod()
