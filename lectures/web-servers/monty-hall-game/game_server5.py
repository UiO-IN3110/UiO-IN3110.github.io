"""
A Basic Monty Hall Game.
========================

Run with
python game_server5.py


Improvements to game_server4.py:

Implements the /final page. Shows the results of the game and a link to start
a new game
"""

import random
import uuid

from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory="templates")

game_states = {}  # Maps game id to winner door


@app.get("/", response_class=HTMLResponse)
def root():
    return """<h1>Welcome to the <b>magic door</b> game!</h1>
<a href="/select">Launch game</a>
"""


@app.get("/select")
def new(request: Request):
    game_id = str(uuid.uuid4())  # Create a unique identifier for this game
    winning = random.randint(1, 3)  # Define a winning door
    game_states[game_id] = winning

    return templates.TemplateResponse(
        "select4.html",
        {
            "request": request,
            "game_id": game_id,
        },
    )


@app.post("/reselect")
def reselect(request: Request, game_id: str, door: int = Form(...)):
    winning = game_states[game_id]

    # Open a random door (but not the winning nor the user-chosen door)
    opened = {1, 2, 3}
    opened.discard(winning)
    opened.discard(door)
    opened = random.choice(list(opened))

    return templates.TemplateResponse(
        "reselect4.html",
        {
            "request": request,
            "game_id": game_id,
            "selected": door,
            "opened": opened,
        },
    )


@app.post("/final")
def final(request: Request, game_id: str, door: int = Form(...)):
    winning = game_states[game_id]

    has_won = door == winning
    return templates.TemplateResponse(
        "final5.html",
        {
            "request": request,
            "has_won": has_won,
            "winning": winning,
        },
    )


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app)
