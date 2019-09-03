#!/usr/bin/env python

from math import sin
import sys

x = float(sys.argv[1])
sinx = sin(x)
print(f"Hello, sin({x:g}) = {sinx:.3f}")
