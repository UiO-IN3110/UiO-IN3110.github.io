class MyNumber:
    def __init__(self, n):
        self.n = n
    
    def __repr__(self):
        return f"MyNumber({self.n})"

    def __add__(self, other):
        if not isinstance(other, MyNumber):
            raise TypeError("Can only add MyNumbers together")
        return MyNumber(self.n + other.n)
    
    def __mul__(self, other):
        if not isinstance(other, MyNumber):
            raise TypeError("Can only multiply MyNumbers together")
        return MyNumber(self.n * other.n)





def test_MyNumberClass():
    a = [2, -4, 10]
    b = [3, 2, 15]
    for n1 in a:
        for n2 in b:
            A = MyNumber(n1)
            B = MyNumber(n2)
            assert n1+n2 == (A+B).n
            assert n1*n2 == (A*B).n
    
