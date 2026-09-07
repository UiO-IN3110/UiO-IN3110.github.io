#!/usr/bin/env python3


class Point:
    """Class representing a 2-D Cartesian point"""

    def __init__(self, x, y): ...

    def __repr__(self):
        return f"Point({self.x}, {self.y})"

    def __add__(self, other):
        """Add two points"""
        ...

    # subtraction
    # what's the subtraction magic method?
    def __whats_subtraction__(self, other):
        """Subtract one point from another"""
        ...

    def __mul__(self, other):
        """Multiply by scalar"""
        ...

    # matrix multiplication
    def __whats_matrix_multiply__(self, other):
        """Dot product of two points, return a scalar"""


a = Point(1, 2)
b = Point(-1, 5)
print(f"a = {a}")
print(f"b = {b}")
print(f"a + b = {a + b}")
print(f"a - b = {a - b}")
print(f"a * 5 = {a * 5}")
print(f"a · b = {a @ b}")
