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
        },
    )


@app.get("/norway_plot.json")
def norway_plot_json():
    print("requesting json chart")


@app.get("/norway_plot.png")
def norway_plot_png():
    print("requesting png ploot")


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app)
