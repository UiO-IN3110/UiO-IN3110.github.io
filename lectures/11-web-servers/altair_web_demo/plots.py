import io
from functools import lru_cache

import altair as alt
import matplotlib
import pandas as pd
import requests

matplotlib.use("agg")

import matplotlib.pyplot as plt

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
    cases["daily cases"] = 0

    for fylke in cases.fylke_name.unique():
        mask = cases.fylke_name == fylke
        fylke_cases = cases.loc[mask]
        diff = fylke_cases.cases.diff()
        # set first value from cases
        diff.iloc[0] = fylke_cases.iloc[0].cases
        cases.loc[fylke_cases.index, "daily cases"] = diff.astype(int)

    # per100k is "daily new cases per 100k population"
    cases["per100k"] = cases["daily cases"] * 1e5 / (cases["population"] + 1)

    # limit data to 2021
    return cases[cases.date.dt.year >= 2021]


def get_fylker():
    """Return unique fylke names"""
    return fylke_data().fylke_name.unique()


ymax = 200


def plot_daily_cases_altair(fylker=None):
    # get data
    cases = fylke_data()
    # if fylker specified, filter data
    if fylker:
        # fylker specified, only display those
        cases = cases[cases.fylke_name.isin(fylker)]

    # altair limits to 5k rows
    if len(cases) > 5000:
        cases = cases[-5000:]

    # return altair Chart
    return (
        alt.Chart(cases)
        .mark_line()
        .encode(
            x="date",
            y=alt.Y(
                "per100k",
                scale=alt.Scale(domain=(0, ymax)),
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


def figure_to_png_bytes(figure):
    """Convert a matplotlib figure to PNG bytes"""
    buf = io.BytesIO()
    # bbox_inches="tight" ensures nothing is cropped,
    # but size can be variable
    figure.savefig(buf, format="png", bbox_inches="tight")
    return buf.getvalue()


def plot_daily_cases_mpl(fylker=None):
    # get data
    cases = fylke_data()
    # if fylker specified, filter data
    if fylker:
        # fylker specified, only display those
        cases = cases[cases.fylke_name.isin(fylker)]

    fig, ax = plt.subplots()
    fig.set_size_inches(10, 8)
    fig.set_dpi(400)

    cases.set_index("date").groupby("fylke_name").per100k.plot(legend=True, ax=ax)
    ax.set_ylim(0, ymax)
    # shift the legend to just outside the right edge
    ax.legend(
        loc="upper left",
        bbox_to_anchor=(1.02, 1),
        borderaxespad=0,
    )
    # return figure rendered as PNG bytes
    return figure_to_png_bytes(fig)
