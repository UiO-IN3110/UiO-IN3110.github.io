"""Serve an altair plot with a form to pick some chart options

via dropdowns

html template is templates/plot.html
"""

import json

import altair as alt

from flask import Flask, render_template, request
from vega_datasets import data

cars = data.cars()

app = Flask(__name__)


@app.route("/")
def main():
    """The main / page serves the plot.html template"""
    return render_template("plot.html")


@app.route("/plot.json", methods=["POST"])
def plot():
    """POST requests to /plot.json

    The body of the request should be JSON
    with keys:

            x-axis: column name for the x axis
            y-axis: column name for the y axis

    The response will be the vega chart spec as JSON
    """
    content = request.json
    chart = (
        alt.Chart(cars)
        .mark_point()
        .encode(
            x=content.get("x-axis", "Horsepower"),
            y=content.get("y-axis", "Miles_per_Gallon"),
            color="Origin",
        )
    )
    return json.dumps(chart.to_dict()), 200, {"Content-Type": "application/json"}


if __name__ == "__main__":
    app.run(port=5001)
