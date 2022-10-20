import pandas as pd
import pytest
from bs4 import BeautifulSoup
from time_planner import extract_events, render_schedule, time_plan

sample_table = """
<table>
  <tr>
    <th>Date</th>
    <th>Venue</th>
    <th>Type</th>
    <th>Info</th>
  </tr>
  <tr>
    <td>October</td>
    <td rowspan="2">UiO</td>
    <td>Assignment 3</td>
    <td>image filters</td>
  </tr>
  <tr>
    <td>November</td>
    <td colspan="2">Assignment 4</td>
  </tr>
</table>
"""


def test_extract_events():

    table = BeautifulSoup(sample_table, "html.parser")
    events = extract_events(table)
    assert isinstance(events, pd.DataFrame)
    assert "Date" in events.columns
    assert "Venue" in events.columns
    assert "Type" in events.columns
    assert len(events) == 2
    assert list(events["Venue"]) == ["UiO", "UiO"]
    assert list(events["Date"]) == ["October", "November"]
    assert list(events["Type"]) == ["Assignment 3", "Assignment 4"]


def test_render_schedule():
    table = BeautifulSoup(sample_table, "html.parser")
    events = extract_events(table)
    print(events)
    md = render_schedule(events)
    print(md)
    assert "<td>" not in md
    assert "<table>" not in md
    assert "UiO" in md
    assert "Assignment 4" in md
    assert "October" in md
    assert "November" in md
    assert md.count("Assignment 4") == 1
    assert md.count("Assignment 3") == 1
    assert md.count("UiO") == 2


@pytest.mark.parametrize(
    "year",
    [
        "2022-23",
        # additional tests may be useful:
        # "2021-22",
        # "2020-21",
    ],
)
def test_time_plan(year):
    url = f"https://en.wikipedia.org/wiki/{year}_FIS_Alpine_Ski_World_Cup"
    markdown = time_plan(url)
    print(markdown)
    assert markdown.count("Downhill") == 15
    assert markdown.count("Sölden") == 1
    assert markdown.count("Beaver Creek") == 3
    assert markdown.count("Méribel") == 3
    assert "19 March 2023" in markdown
    assert "23 October 2022" in markdown
