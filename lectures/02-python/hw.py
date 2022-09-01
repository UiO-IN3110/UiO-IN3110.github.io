#!/usr/bin/env python3

from math import sin
import sys

x = float(sys.argv[1])
sin_x = sin(x)

print(f"Hello, sin({x:g}) = {sin_x:.3f}")

