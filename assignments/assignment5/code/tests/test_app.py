import datetime
from urllib.parse import urlencode

import pandas as pd
import pytest
from bs4 import BeautifulSoup

location_codes = {f"NO{i}" for i in range(1, 6)}


def get_content_type(response):
    """Return the content-type of an HTTP response

    text/html or application.json

    (without trailing `; charset=utf-8`)
    """
    content_type = response.headers["Content-Type"]
    return content_type.split(";", 1)[0].strip()


def test_main_page(client):
    response = client.get("/")
    assert response.status_code == 200
    content_type = get_content_type(response)
    assert content_type == "text/html"
    # check for some expected elements
    page = BeautifulSoup(response.text, "html.parser")
    assert page.title.text == "Strømpris"


def test_form_input(client):
    response = client.get("/")
    # check for some expected elements
    page = BeautifulSoup(response.text, "html.parser")
    form = page.find("form", id="price-form")
    # check end input
    end_input = form.find("input", attrs={"name": "end"})
    assert end_input, "Missing input for `name=end`"
    assert end_input["type"] == "date", "end date input should have type=date"
    # could check min, max but these aren't required

    # check days input
    days_input = form.find("input", attrs={"name": "days"})
    assert days_input, "Missing input for `name=days`"
    assert days_input["type"] == "number", "days input should have type=number"

    # check location inputs
    locations_inputs = form.find_all("input", attrs={"name": "locations"})
    assert locations_inputs

    location_values = []
    for location_input in locations_inputs:
        assert (
            location_input["type"] == "checkbox"
        ), "locations inputs should have type=checkbox"
        location_values.append(location_input.attrs.get("value"))

    assert sorted(location_values) == sorted(location_codes)

    assert page.title.text == "Strømpris"


@pytest.mark.parametrize(
    "locations, end, days",
    [
        (None, None, None),
        [["NO1"], "2022-11-05", 2],
        [["NO1", "NO2"], "2022-11-03", 1],
    ],
)
def test_plot_prices_json(client, locations, end, days):
    params = {}
    if locations:
        params["locations"] = locations
    else:
        locations = sorted(location_codes)
    if end:
        params["end"] = end
    else:
        end = datetime.date.today().isoformat()
    if days:
        params["days"] = days
    else:
        days = 7

    end_date = datetime.date.fromisoformat(end)

    url = "/plot_prices.json?" + urlencode(params, doseq=True)
    print(f"Fetching {url}")

    response = client.get(url)
    assert response.status_code == 200
    content_type = get_content_type(response)
    assert content_type == "application/json"
    chart_data = response.json()
    # load datasets
    dataframes = [
        pd.DataFrame.from_dict(data) for data in chart_data["datasets"].values()
    ]
    for df in dataframes:
        assert "time_start" in df.columns
        assert "location" in df.columns
        assert "location_code" in df.columns

        assert set(df.location_code.unique()) == set(locations)
        time_start = pd.to_datetime(df.time_start)
        assert time_start.max().date() == end_date
        assert time_start.min().date() == end_date - datetime.timedelta(days=days - 1)
