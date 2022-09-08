from typing import List
import math


def is_prime(n:int) -> int:
    '''Check if n is a prime number'''
    assert isinstance(n, int)
    assert n > 0
    
    for x in range(2, int(math.sqrt(n) + 1)):
        if n % x == 0: 
            return False
    return True

Vector = List[float]

from IPython import embed


def prime_factors(n: int) -> Vector:
    '''Increasing sequence of prime factors of n'''

    if is_prime(n): return [n]

    for m in range(2, n):
        if is_prime(m) and n % m == 0:
            return [m] + prime_factors(n//m)

# --------------------------------------------------------------------

if __name__ == '__main__':
    import pdb
    pdb.set_trace()
        
    print(prime_factors(30))
