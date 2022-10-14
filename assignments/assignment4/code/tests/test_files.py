from pathlib import Path

import pytest


@pytest.fixture
def assignment4():
    return Path(__file__).parent.parent.resolve()


def test_location(assignment4):
    # check that we're in repo root/assignment4
    assert (
        assignment4.name == "assignment4"
    ), "Assignment is not in the correct `assignment4` directory!"


@pytest.mark.parametrize(
    "filename",
    [
        "README.md",
        "requesting_urls.py",
        "filter_urls.py",
        "collect_dates.py",
        "time_planner.py",
        # "wiki_race_challenge.py",
    ],
)
def test_files_exist(assignment4, filename):
    assert assignment4.joinpath(filename).exists()
