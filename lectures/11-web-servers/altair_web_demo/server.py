import datetime
from typing import List, Optional

import plots
from fastapi import FastAPI, Query, Request
from fastapi.responses import Response
from fastapi.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory="templates")


@app.get("/")
def norway_plot_html(request: Request):
    return templates.TemplateResponse(
        "norway_plot.html",
        {
            "request": request,
            "fylker": plots.get_fylker(),
            "date": str(datetime.date.today()),
        },
    )


@app.get("/norway_plot.json")
def norway_plot_json(fylker: Optional[List[str]] = Query(default=None)):
    # altair Chart.to_dict() is a JSONable vega-lite structure
    fig = plots.plot_daily_cases_altair(fylker)
    return fig.to_dict()


@app.get("/norway_plot.png")
def norway_plot_png(fylker: Optional[List[str]] = Query(default=None)):
    png_bytes = plots.plot_daily_cases_mpl(fylker)
    return Response(
        content=png_bytes,
        media_type="image/png",
    )


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, port=9000)
