"""
A Basic Monty Hall Game.
========================

Run with
python game_server2.py


Improvements to game_server1.py:
- /select URL implemented and and rendered from a template.
- The template contains a form with a POST request to the /reselect.
"""

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
def root():
    return """<h1>Welcome to the <b>magic door</b> game!</h1>
<a href="/select">Launch game</a>
"""


@app.get("/select", response_class=HTMLResponse)
def new(request: Request):
    return templates.TemplateResponse("select2.html", {"request": request})


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app)
