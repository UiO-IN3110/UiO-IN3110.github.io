from time import sleep
from IPython import embed

def slow_mult(x,y):
    res = 0
    for i in range(y):
        print("Thinking...")
        sleep(1)
        res += x
    return res

def memoize(func):
    memory = {}
    def inner(x,y):
        if (x,y) in memory:
            return memory[(x,y)]
        elif (y,x) in memory:
            return memory[(y,x)]
        else:
            result = func(x,y)
            memory[(x,y)] = result
            return result
    return inner
    
fast_mult = memoize(slow_mult)

print(fast_mult(2,3))
print(fast_mult(3,2))

