#!/usr/bin/env python3

import sys
from math import sin

x = float(sys.argv[1])
sin_x = sin(x)

print(f"Hello, sin({x:g}) = {sin_x:.3f}")
