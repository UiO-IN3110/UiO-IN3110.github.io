from setuptools import setup

# IN4110: set to True when you are ready for the Cython implementation in Task 5
use_cython = False


if use_cython:
    from setuptools import Extension
    import numpy as np
    from Cython.Build import cythonize

    extensions = [
        # A single module that is stand alone and has no special requisites
        Extension(
            "instapy.cython_filters",
            ["instapy/cython_filters.pyx"],
            include_dirs=[
                np.get_include(),
            ],
            # enable profiling
            define_macros=[
                ("CYTHON_TRACE", "1"),
                ("CYTHON_TRACE_NOGIL", "1"),
            ],
        ),
    ]
    cython_directives = {
        "language_level": 3,
        # enable profiling
        "binding": True,
        "profile": True,
        "linetrace": True,
        # you may want to add some compiler directives here
        # to optimize compilation
    }
    ext_modules = cythonize(
        extensions,
        compiler_directives=cython_directives,
        annotate=True,
    )
else:
    ext_modules = []

setup(ext_modules=ext_modules)
