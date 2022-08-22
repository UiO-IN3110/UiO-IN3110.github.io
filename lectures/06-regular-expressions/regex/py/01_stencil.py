"""
Simple stencil calculations.
::
                              X[ i  j-2]
                 X[i-1 j-1]   X[ i  j-1]   X[i+1 j-1]
    X[i-2  j ]   X[i-1  j ]   X[ i   j ]   X[i+1  j ]   X[i+2  j ]
                 X[i-1 j+1]   X[ i  j+1]   X[i+1 j+1]
                              X[ i  j+2]
"""
import numpy


def inner_stencil(arr: numpy.narray, i: int, j: int) -> float:
    """Calculate the inner tensile core."""
    out = 8*arr[j, i]
    out -= 5*arr[j+1, i]
    out -= 5*arr[j-1, i]
    out -= 3*arr[j, i+1]
    out -= 3*arr[j, i-1]
    out += 2*arr[j-2, i]
    out += 2*arr[j+2, i]
    out += arr[j, i+2]
    out += arr[j, i-2]
    out += arr[j-1, i-1]
    out += arr[j-1, i+1]
    out += arr[j+1, i-1]
    out += arr[j+1, i+1]

    return out
