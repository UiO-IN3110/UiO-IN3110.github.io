from math import log

def f(x):
    return log(x) - 2

def checkrange(func):
    def inner(x):
        if x <= 0:
            print('x has to be greater than zero')
        else: 
            return func(x)
    return inner


def test_range():
    f_safe = checkrange(f)
    assert f_safe(2) == f(2)
    assert f_safe(-1) == None

