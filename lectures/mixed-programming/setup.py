from Cython.Build import cythonize
from setuptools import setup

setup(
    name="in3110-cython",
    ext_modules=cythonize(
        ["integral*.py", "apply.py"],
        language_level=3,
        annotate=True,
    ),
)
