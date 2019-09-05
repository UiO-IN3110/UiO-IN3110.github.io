#!/usr/bin/env python

from IPython import embed
from math import sin
import sys

x = float(sys.argv[1])
sinx = sin(x)

embed()

print(f"Hello, sin({x:g}) = {sinx:.3f}")
