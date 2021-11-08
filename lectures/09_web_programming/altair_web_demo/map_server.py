from typing import Optional

from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from plots import get_fylker, plot_daily_cases

app = FastAPI()
templates = Jinja2Templates(directory="templates")


@app.get("/")
def norway_plot_html(request: Request):
    return templates.TemplateResponse(
        "norway_plot.html",
        {
            "request": request,
            "fylker": get_fylker(),
        },
    )


@app.get("/norway_plot.json")
def norway_plot_json(fylker: Optional[str] = None):
    # fylker is a query param, a comma-separated list
    if fylker:
        fylker = fylker.split(",")
    # altair Chart.to_dict() is a JSONable vega-lite structure
    fig = plot_daily_cases(fylker)
    return fig.to_dict()


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app)
