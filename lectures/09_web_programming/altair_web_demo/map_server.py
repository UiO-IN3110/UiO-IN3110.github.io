import json
import tempfile

from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from plots import norway_plot

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
    fig = norway_plot()

    tmp = tempfile.NamedTemporaryFile(suffix=".json")
    fig.save(tmp.name)

    with open(tmp.name) as file:
        return json.load(file)


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app)
