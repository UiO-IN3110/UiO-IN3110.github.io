#!/usr/bin/env python

import os
import uuid

from flask import Flask
from flask import render_template
from flask import request
import monty_hall_game
from monty_hall_game import MontyHallGame

templates = os.path.join(os.path.dirname(monty_hall_game.__file__), "templates")

app = Flask("MontyHallGame", template_folder=templates)


@app.route("/")
def root():
    return """<h1>Welcome to the <b>magic door</b> game!</h1>
<a href="/select/">Launch game</a>
"""


games = {}


@app.route("/select/")
def new():
    game_id = str(uuid.uuid4())
    game = MontyHallGame()
    games[game_id] = game

    return render_template("select.html", game_id=game_id)


@app.route("/reselect", methods=["POST"])
def reselect():

    # request.args contains the URL parameters, like the game_id
    game_id = request.args.get("game_id")
    game = games[game_id]

    # request.form contains all form parameters, like the selected door
    selected = int(request.form["door"])
    game.select_door(selected)

    # Open a random door (but not the winning nor the user-chosen door)
    opened = game.let_host_open_door()

    return render_template(
        "reselect.html", game_id=game_id, selected=selected, opened=opened
    )


@app.route("/final", methods=["POST"])
def final():
    # request.args contains the URL parameters, like the game_id
    game = games[request.args.get("game_id")]

    # request.form contains all form parameters, like the selected door
    selected = int(request.form["door"])
    game.select_door(selected)

    has_won = game.open_door()

    return render_template("final.html", has_won=has_won, winning=game.winning_door())


@app.route("/statistics")
def statistics():
    stats = MontyHallGame.statistics().replace("\n", "</br>")

    return "<h1>Statistics</h1>{}".format(stats)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
