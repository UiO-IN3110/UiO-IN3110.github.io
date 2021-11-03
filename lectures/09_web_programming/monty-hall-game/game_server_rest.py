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
from functools import partial
from typing import Optional

from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel, Field

app = FastAPI()

game_states = {}  # Maps game id to winner door


class MontyHallGame(BaseModel):
    """Represents a Monty Hall game state"""

    winning: int = Field(default_factory=partial(random.randint, 1, 3))
    first_choice: Optional[int]
    opened: Optional[int]
    second_choice: Optional[int]
    has_won: Optional[bool]

    def choose(self, choice: int):
        """The first step: Make a choice"""
        self.first_choice = choice

    def reveal(self):
        """The second step: host reveals a door that definitely has a goat."""
        choices = set([1, 2, 3])
        # don't open the winning door
        choices.discard(self.winning)
        # don't open the door they've already chosen
        choices.discard(self.first_choice)
        # open a random remaining door.
        # there is either 1 or 2 choices left
        self.opened = random.choice(list(choices))
        return self.opened

    def choose_again(self, switch: bool):
        """Guest can either switch to the other door, or stay with their first choice"""
        if switch:
            choices = set([1, 2, 3])
            choices.discard(self.first_choice)
            choices.discard(self.opened)
            self.second_choice = choices.pop()
        else:
            self.second_choice = self.first_choice
        self.has_won = self.second_choice == self.winning
        return self.second_choice


class NewGame(BaseModel):
    id: str


@app.post("/games", response_model=NewGame)
def new_game():
    game_id = str(uuid.uuid4())  # Create a unique identifier for this game
    # store a Game object for the id
    game_states[game_id] = MontyHallGame()
    # return a model with the identifier


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app)
