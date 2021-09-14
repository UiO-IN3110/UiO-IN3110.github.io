from time import sleep
from IPython import embed

def slow_mult(x,y):
    res = 0
    for i in range(y):
        print("Thinking...")
        sleep(1)
        res += x
    return res




