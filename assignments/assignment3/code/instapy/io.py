"""input/output utilities

for reading, writing, and displaying image files
as numpy arrays
"""

import numpy as np
from PIL import Image


def read_image(filename: str) -> np.array:
    """Read an image file to an rgb array"""
    return np.asarray(Image.open(filename))


def write_image(array: np.array, filename: str) -> None:
    """Write a numpy pixel array to a file"""
    return Image.fromarray(array).save(filename)


def random_image(width: int = 320, height: int = 180) -> np.array:
    """Create a random image array of a given size"""
    return np.random.randint(0, 255, size=(height, width, 3), dtype=np.uint8)


def display(array: np.array):
    """Show an image array on the screen"""
    Image.fromarray(array).show()
