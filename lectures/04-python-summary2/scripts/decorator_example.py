from math import log

def checkrange(func):
    def inner(x):
        if x <= 0:
            print('Error: x must be larger than zero')
        else:
            return f(x)
    return inner


def f(x):
    return log(x) - 2


