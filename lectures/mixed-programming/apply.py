import numpy as np
from cython import double, int
from cython.cimports.libc.math import sin


def apply_sin(a: double[:]) -> double[:]:
    i: int
    out: double[:] = np.empty_like(a)

    for i in range(len(a)):
        out[i] = sin(a[i])

    return out
