class Polynomial:

    def __init__(self, coefficients):
        """coefficients should be a list of numbers with 
        the i-th element being the coefficient a_i."""
        
        raise NotImplemented

    def degree(self):
        """Return the index of the highest nonzero coefficient.
        If there is no nonzero coefficient, return -1."""
        
        raise NotImplemented

    def coefficients(self):
        """Return the list of coefficients. 

        The i-th element of the list should be a_i, meaning that the last 
        element of the list is the coefficient of the highest degree term."""
        
        raise NotImplemented

    def __call__(self, x):
        """Return the value of the polynomial evaluated at the number x"""

        raise NotImplemented

    
    def __add__(self, p):
        """Return the polynomial which is the sum of p and this polynomial
        Should assume p is Polynomial([p]) if p is int. 

        If p is not an int or Polynomial, should raise ArithmeticError."""

        raise NotImplemented
        
    def __sub__(self, p):
        """Return the polynomial which is the difference of p and this polynomial
        Should assume p is Polynomial([p]) if p is int. 

        If p is not an int or Polynomial, should raise ArithmeticError."""

        raise NotImplemented

    def __mul__(self, c):
        """Return the polynomial which is this polynomial multiplied by given integer.
        Should raise ArithmeticError if c is not an int."""

        raise NotImplemented


    def __rmul__(self, c):
        """Return the polynomial which is this polynomial multiplied by some integer"""

        raise NotImplemented
    
    def __repr__(self):
        """Return a nice string representation of polynomial.
        
        E.g.: x^6 - 5x^3 + 2x^2 + x - 1
        """
        raise NotImplemented

    def __eq__(self, p):
        """Check if two polynomials have the same coefficients."""

        raise NotImplemented

def sample_usage():
    p = Polynomial([1, 2, 1]) # 1 + 2x + x^2
    q = Polynomial([9, 5, 0, 6]) # 9 + 5x + 6x^3
    
    
    print("The value of {} at {} is {}".format(p, 7, p(7)))

    print("The coefficients of {} are {}".format(p, p.coefficients()))

    
    print("\nAdding {} and {} yields {}".format(p, q, p+q))

    p, q, r = map(Polynomial,
                  [
                      [1, 0, 1], [0, 2, 0], [1, 2, 1]
                  ]
    )
    
    print("\nWill adding {} and {} be the same as {}? Answer: {}".format(
        p, q, r, p+q == r
    ))
    print("\nIs {} - {} the same as {}? Answer: {}".format(
        p, q, r, p-q == r
    ))
