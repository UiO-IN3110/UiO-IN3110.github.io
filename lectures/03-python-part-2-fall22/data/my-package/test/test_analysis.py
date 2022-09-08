from pkg.analysis import is_prime
import pytest


def test_prime_sanity():
    assert is_prime(2)
    assert is_prime(5)
    assert is_prime(7)     

    assert not is_prime(8)     

    
def test_prime_inputchecks():
    with pytest.raises(AssertionError):
        is_prime(2.1)

    with pytest.raises(AssertionError):
        is_prime(-1)


from pkg.analysis import prime_factors        

@pytest.mark.parametrize('x, y', [(x, x) for x in (1, 2, 3, 5, 7)])
def test_prime_factors_primes(x, y):
    assert prime_factors(x) == [y]


def test_prime_factors_composites():
   assert prime_factors(6) == [2, 3]
   assert prime_factors(8) == [2, 2, 2]
   assert prime_factors(10) == [2, 5]        
