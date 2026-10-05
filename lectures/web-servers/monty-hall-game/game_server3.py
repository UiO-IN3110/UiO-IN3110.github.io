"""
A Basic Monty Hall Game.
========================

Run with
python game_server3.py


Improvements to game_server2.py:

- /reselect endpoint is implemented. It receives the selected door as a the POST request
  and displays it in the reselect3.html template
"""

from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
def root():
    return """<h1>Welcome to the <b>magic door</b> game!</h1>
<a href="/select">Launch game</a>
"""


@app.get("/select")
def new(
    request: Request,
):
    return templates.TemplateResponse(
        "select2.html",
        {
            "request": request,
        },
    )


@app.post("/reselect")
def reselect(request: Request, door: int = Form(...)):
    return templates.TemplateResponse(
        "reselect3.html", {"request": request, "selected": door}
    )


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app)
