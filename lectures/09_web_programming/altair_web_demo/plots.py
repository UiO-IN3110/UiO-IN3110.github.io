import io
from functools import lru_cache

import altair as alt
import pandas as pd
import requests

data_url = "https://raw.githubusercontent.com/thohan88/covid19-nor-data/HEAD/data"


def download_dataset(
    path,
    parse_dates=[
        "date",
    ],
    data_url=data_url,
):
    """Download a dataset from covid19-nor-data archive"""
    url = f"{data_url}/{path}"
    print(f"Downloading {url}")
    r = requests.get(f"{data_url}/{path}")
    r.raise_for_status()
    print(f"Downloaded {len(r.content) // 1024}kB")
    return pd.read_csv(io.BytesIO(r.content), parse_dates=parse_dates)


@lru_cache()
def fylke_data():
    # get raw case data
    cases = all_cases = download_dataset(
        "01_infected/msis/municipality_and_district.csv"
    )

    # aggregate data by fylke
    cases = (
        all_cases.groupby(["fylke_name", "date"])[["cases", "population"]]
        .sum()
        .reset_index()
    )
    # discard ukjent fylke where per 100k doesn't make sense
    cases = cases[~cases.fylke_name.str.contains("Ukjent")]

    # 'cases' is a cumulative sum
    # reverse that to calculate the daily new case count
    cases["new cases"] = 0.0

    for fylke in cases.fylke_name.unique():
        mask = cases.fylke_name == fylke
        fylke_cases = cases.loc[mask]
        cases.loc[fylke_cases.index, "new cases"] = fylke_cases.cases.diff()

    # per100k is "daily new cases per 100k population"
    cases["per100k"] = cases["new cases"] * 1e5 / (cases["population"] + 1).astype(int)

    # limit data to 2021
    return cases[cases.date.dt.year >= 2021]


def get_fylker():
    """Return unique fylke names"""
    return fylke_data().fylke_name.unique()


def plot_daily_cases(fylker=None):
    # get data
    cases = fylke_data()
    # if fylker specified, filter data
    if fylker:
        # fylker specified, only display those
        cases = cases[cases.fylke_name.isin(fylker)]

    # return altair Chart
    return (
        alt.Chart(cases)
        .mark_line()
        .encode(
            x="date",
            y=alt.Y(
                "per100k",
                scale=alt.Scale(domain=(0, 100)),
            ),
            color="fylke_name",
            tooltip=[
                "date",
                "fylke_name",
                "per100k",
                "cases",
                "population",
            ],
        )
        .interactive()
    )
