from cProfile import profile
from time import time

from numpy import arange


@profile  # noqa: F821
def sum2d(arr):
    M, N = arr.shape
    result = 0.0

    for i in range(M):
        for j in range(N):
            result += arr[i, j]

    return result


N = 1000
a = arange(N**2).reshape(N, N)

t0 = time()
sum2d(a)
t1 = time()

print(f"Runtime: {t1-t0} s")
