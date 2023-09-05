import math
from typing import List


def is_prime(n: int) -> int:
    """Check if n is a prime number"""
    assert isinstance(n, int)
    assert n > 0

    for x in range(2, int(math.sqrt(n) + 1)):
        if n % x == 0:
            return False
    return True


Vector = List[float]


def prime_factors(n: int) -> Vector:
    """Increasing sequence of prime factors of n"""

    if is_prime(n):
        return [n]

    for m in range(2, n):
        if n % m == 0 and is_prime(m):
            return [m] + prime_factors(n // m)


# --------------------------------------------------------------------

if __name__ == "__main__":
    import pdb

    pdb.set_trace()

    print(prime_factors(30))
