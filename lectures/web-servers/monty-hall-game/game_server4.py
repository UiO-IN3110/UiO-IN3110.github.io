"""
A Basic Monty Hall Game.
========================

Run with
python game_server4.py


Improvements to game_server3.py:

- Implement state as a module-wide dictionary game_state. When a new game is
started, we create a unique game_id and draw a random winning door and attach
it to the state. In the form in the select4.html template, we now pass the
game_id as a URL parameter to /reselect. In the reselect function we can use
the request.get and request.form attributes to extract both the game_id and
the user selected door. With that, we can implement the logic of the host to
open a door (which is not the winning door).

The result is rendered in the reselect in the reselect4.html page, where we
also added a form to pick another door. This form sends a POST request to
/final (again with the game_id attached)

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


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app)
