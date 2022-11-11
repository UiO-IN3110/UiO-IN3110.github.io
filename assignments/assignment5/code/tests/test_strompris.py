import datetime

import altair as alt
import pytest
from strompris import fetch_day_prices, fetch_prices, plot_daily_prices, plot_prices

location_codes = {f"NO{i}" for i in range(1, 6)}


def test_fetch_day_prices_defaults():
    df_default = fetch_day_prices()
    df_expected = fetch_day_prices(date=datetime.date.today(), location="NO1")
    assert (df_default.time_start == df_expected.time_start).all()
    assert (df_default.NOK_per_kWh == df_expected.NOK_per_kWh).all()


def test_fetch_day_prices_columns():
    df = fetch_day_prices()
    assert "time_start" in df.columns
    assert "NOK_per_kWh" in df.columns
    assert isinstance(df.NOK_per_kWh[0], float)
    assert isinstance(df.time_start[0], datetime.datetime)


@pytest.mark.parametrize(
    "date, location",
    [
        (datetime.date(2022, 10, 2), "NO1"),
        (datetime.date(2022, 11, 10), "NO5"),
    ],
)
def test_fetch_day_prices(date, location):
    df = fetch_day_prices(date=date, location=location)
    assert (df.time_start.dt.date == date).all()


def test_fetch_prices_default():
    df_default = fetch_prices()
    df_expected = fetch_prices(
        end_date=datetime.date.today(),
        days=7,
        locations=[f"NO{i}" for i in range(1, 6)],
    )
    assert len(df_default) == len(df_expected)
    assert set(df_default.location_code.unique()) == location_codes
    assert df_default.time_start.max() == df_expected.time_start.max()
    assert df_default.time_start.min() == df_expected.time_start.min()


def test_fetch_prices():
    date = datetime.date(2022, 11, 5)
    location = "NO1"
    df_day = fetch_day_prices(date)
    df = fetch_prices(end_date=date, days=1, locations=[location])
    assert "location" in df.columns
    assert "location_code" in df.columns
    assert (df["location"] == "Oslo").all()
    assert (df["location_code"] == "NO1").all()
    assert (df["time_start"] == df_day["time_start"]).all()


def test_plot_prices():
    # this test doesn't verify much of the output,
    # only that the function works without error
    df = fetch_prices(
        end_date=datetime.date(2022, 10, 30), days=3, locations=["NO1", "NO2"]
    )
    chart = plot_prices(df)
    assert isinstance(chart, alt.Chart)
    chart_dict = chart.to_dict()
    assert chart.mark == "line"
    # could assert encodings here


def test_plot_daily_prices():
    # this test doesn't verify the output,
    # only that the function works
    df = fetch_prices(
        end_date=datetime.date(2022, 10, 30), days=3, locations=["NO1", "NO2"]
    )
    chart = plot_daily_prices(df)
    assert isinstance(chart, alt.Chart)
    chart_dict = chart.to_dict()
    # could assert encodings here
