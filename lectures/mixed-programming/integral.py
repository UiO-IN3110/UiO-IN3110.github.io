import cython as C
from cython.cimports.libc.math import sin


@C.cfunc
@C.nogil
def f(x: C.double) -> C.double:
    return sin(x**2)


def integrate_f(a: C.double, b: C.double, N: C.int) -> C.double:
    s: C.double = 0
    dx: C.double = (b - a) / N
    i: C.int
    for i in range(N):
        s += f(a + i * dx)
    return s * dx
