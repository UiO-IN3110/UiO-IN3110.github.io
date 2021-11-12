from typing import Optional

from fastapi import FastAPI, Request
from fastapi.responses import Response
from fastapi.templating import Jinja2Templates
import plots

app = FastAPI()
templates = Jinja2Templates(directory="templates")


@app.get("/")
def norway_plot_html(request: Request):
    return templates.TemplateResponse(
        "norway_plot.html",
        {
            "request": request,
            "fylker": plots.get_fylker(),
        },
    )


@app.get("/norway_plot.json")
def norway_plot_json(fylker: Optional[str] = None):
    # fylker is a query param, a comma-separated list
    if fylker:
        fylker = fylker.split(",")
    # altair Chart.to_dict() is a JSONable vega-lite structure
    fig = plots.plot_daily_cases_altair(fylker)
    return fig.to_dict()


@app.get("/norway_plot.png")
def norway_plot_png(fylker: Optional[str] = None):
    # fylker is a query param, a comma-separated list
    if fylker:
        print(repr(fylker))
        fylker = fylker.split(",")
    # altair Chart.to_dict() is a JSONable vega-lite structure
    png_bytes = plots.plot_daily_cases_mpl(fylker)
    return Response(
        content=png_bytes,
        media_type="image/png",
    )


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app)
