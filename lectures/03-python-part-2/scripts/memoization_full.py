from time import sleep
from IPython import embed

def slow_mult(x,y):
    res = 0
    for i in range(y):
        print("Thinking...")
        sleep(1)
        res += x
    return res

def memoization(f):
    cache = {}
    def inner(x, y):
        if (x,y) in cache:
            return cache[(x,y)]
        else:
            result = f(x,y)
            cache[(x,y)] = result
            return result
    return inner


print(slow_mult(3,3))
print(slow_mult(3,3))

fast_mult = memoization(slow_mult)

#print(fast_mult(3,3))
#print(fast_mult(3,3))
