import numpy
from setuptools import setup
from Cython.Build import cythonize

setup(
    name='in3110-cython',
    ext_modules=cythonize("*.pyx"),
    include_dirs=[numpy.get_include()],
)