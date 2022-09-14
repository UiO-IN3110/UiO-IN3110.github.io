"""Basic tests for the package

Tests that the package is installed and importable.

These tests should pass after task 1,
before you've done any implementation.
"""
from pathlib import Path
import pkg_resources

import numpy as np
import pytest

test_dir = Path(__file__).absolute().parent


def test_import():
    """Can we import our package at all"""
    import instapy  # noqa


def test_install_metadata():
    """Was the package metadata installed?

    Unlike import, this will not pass if `instapy`
    is on PYTHONPATH but `pip install` has not been called.
    """
    try:
        pkg = pkg_resources.get_distribution("instapy")
    except Exception:
        assert (
            False
        ), "No package named `instapy` found. Did you set `project=` in pyproject.toml?"


@pytest.mark.parametrize(
    "dep",
    [
        "numpy",
        "pillow",
        "numba",
    ],
)
def test_dependencies(dep):
    pkg = pkg_resources.get_distribution("instapy")
    pkg_dep_names = [r.name.lower() for r in pkg.requires()]
    assert dep in pkg_dep_names


@pytest.mark.parametrize(
    "filter_name",
    ["color2gray", "color2sepia"],
)
@pytest.mark.parametrize(
    "implementation",
    ["python", "numpy", "numba"],
)
def test_get_filter(filter_name, implementation):
    """Can we load our filter functions"""
    import instapy  # noqa

    filter_function = instapy.get_filter(filter_name, implementation)


def test_io():
    """Can we import and use our io utilities"""
    from instapy import io

    image = io.read_image(test_dir.joinpath("rain.jpg"))
    assert isinstance(image, np.ndarray)
    assert len(image.shape) == 3
    assert image.dtype == np.uint8
    assert image.shape[2] == 3
