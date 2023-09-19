from math import sin

import cython as C


def f(x: C.double) -> C.double:
    return sin(x**2)


def integrate_f(a: C.double, b: C.double, N: C.int) -> C.double:
    s: C.double = 0
    dx: C.double = (b - a) / N
    i: C.int
    for i in range(N):
        s += f(a + i * dx)
    return s * dx
