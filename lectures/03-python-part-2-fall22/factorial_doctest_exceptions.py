def factorial(n: int) -> int:
    '''Return the factorial of n, an exact integer >= 0.

    Args:
       n (int):  n!

    Returns:
       int.  The factorial value::

    >>> factorial(5)
    120
    >>> factorial(0)
    1
    >>> factorial(-1)
    Traceback (most recent call last):
        ...
    ValueError: Only non-negative inputs are expected
    '''
    assert isinstance(n, int)

    if n < 0:
        raise ValueError('Only non-negative inputs are expected')
    
    if n == 0:
        return 1
    return n*factorial(n-1)

# --------------------------------------------------------------------

if __name__ == '__main__':
    import doctest
    doctest.testmod()
