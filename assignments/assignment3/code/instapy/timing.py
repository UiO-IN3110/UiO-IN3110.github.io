"""
Timing our filter implementations.

Can be executed as `python3 -m instapy.timing`

For Task 6.
"""
import time
import instapy
from . import io
from typing import Callable
import numpy as np


def time_one(filter_function: Callable, *arguments, calls: int = 3) -> float:
    """Return the time for one call

    When measuring, repeat the call `calls` times,
    and return the average.

    Args:
        filter_function (callable):
            The filter function to time
        *arguments:
            Arguments to pass to filter_function
        calls (int):
            The number of times to call the function,
            for measurement
    Returns:
        time (float):
            The average time (in seconds) to run filter_function(*arguments)
    """
    # run the filter function `calls` times
    # return the _average_ time of one call
    ...


def make_reports(filename: str = "test/rain.jpg", calls: int = 3):
    """
    Make timing reports for all implementations and filters,
    run for a given image.

    Args:
        filename (str): the image file to use
    """

    # load the image
    image = ...
    # print the image name, width, height
    ...
    # iterate through the filters
    filter_names = ...
    for filter_name in filter_names:
        # get the reference filter function
        reference_filter = ...
        # time the reference implementation
        reference_time = ...
        print(
            f"Reference (pure Python) filter time {filter_name}: {reference_time:.3}s ({calls=})"
        )
        # iterate through the implementations
        implementations = ...
        for implementation in implementations:
            filter = ...
            # time the filter
            filter_time = ...
            # compare the reference time to the optimized time
            speedup = ...
            print(
                f"Timing: {implementation} {filter_name}: {filter_time:.3}s ({speedup=:.2f}x)"
            )


if __name__ == "__main__":
    # run as `python -m instapy.timing`
    make_reports()
