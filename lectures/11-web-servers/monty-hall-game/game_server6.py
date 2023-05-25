"""
A Basic Monty Hall Game.
========================

Run with
python game_server6.py


Improvements to game_server5.py:

Implement a /statistics page that computes the win/loss chances of all played
games. For that, I needed to extend the game_state to store all game
information
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
    game_states[game_id] = {"winning": winning}

    return templates.TemplateResponse(
        "select4.html",
        {
            "request": request,
            "game_id": game_id,
        },
    )


@app.post("/reselect")
def reselect(request: Request, game_id: str, door: int = Form(...)):
    state = game_states[game_id]
    state["first_choice"] = door
    winning = state["winning"]

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
    state = game_states[game_id]
    state["changed_choice"] = door != state["first_choice"]
    winning = state["winning"]
    has_won = door == winning
    state["won"] = has_won

    return templates.TemplateResponse(
        "final5.html",
        {
            "request": request,
            "has_won": has_won,
            "winning": winning,
        },
    )


@app.get("/statistics", response_class=HTMLResponse)
def statistics():
    games = [e for e in game_states.values() if "won" in e]

    changed_and_won = [e["won"] for e in games if e["changed_choice"]]
    notchanged_and_won = [e["won"] for e in games if not e["changed_choice"]]

    changed_sucess_rate = (
        100 * sum(changed_and_won) / len(changed_and_won)
        if len(changed_and_won) > 0
        else 0
    )
    notchanged_success_rate = (
        100 * sum(notchanged_and_won) / len(notchanged_and_won)
        if len(notchanged_and_won) > 0
        else 0
    )

    s1 = "Changed and won: {} out of {} ({}% success)".format(
        sum(changed_and_won), len(changed_and_won), changed_sucess_rate
    )
    s2 = "Not changed and won: {} out of {} ({}% success)".format(
        sum(notchanged_and_won), len(notchanged_and_won), notchanged_success_rate
    )
    return f"<h1>Statistics</h1>{s1}</br>{s2}"


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app)
