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

from flask import Flask
from flask import render_template
from flask import request
import random
import uuid

app = Flask(__name__)

game_states = {}  # Maps game id to winner door

@app.route("/")
def root():
        return """<h1>Welcome to the <b>magic door</b> game!</h1>
<a href="/select/">Launch game</a>
"""

@app.route("/select/")
def new():
    game_id = str(uuid.uuid4())
    winning = random.randint(1, 3)
    game_states[game_id] = {"winning": winning}

    return render_template('select4.html', game_id=game_id)

@app.route('/reselect', methods=['POST'])
def reselect():

    # request.form contains all form parameters, like the selected door
    selected = int(request.form["door"])

    # request.args contains the URL parameters, like the game_id
    game_id = request.args.get("game_id")

    # Record some statistics
    game_states[game_id]["first_choice"] = selected

    winning = game_states[game_id]["winning"]

    # Open a random door (but not the winning nor the user-chosen door)
    opened = set([1, 2, 3])
    opened.discard(winning)
    opened.discard(selected)
    opened = random.choice(list(opened))

    return render_template("reselect4.html", game_id=game_id, selected=selected, opened=opened)

@app.route('/final', methods=['POST'])
def final():

    # request.form contains all form parameters, like the selected door
    selected = int(request.form["door"])

    # request.args contains the URL parameters, like the game_id
    game_id = request.args.get("game_id")
    winning = game_states[game_id]["winning"]

    has_won = selected == winning

    # Record some statistics
    game_states[game_id]["changed_choice"] = selected != game_states[game_id]["first_choice"]
    game_states[game_id]["won"] = has_won

    return render_template("final.html", has_won=has_won, winning=winning)

@app.route('/statistics')
def statistics():
    changed_and_won = [e["won"] for e in game_states.values() if e["changed_choice"]]
    notchanged_and_won = [e["won"] for e in game_states.values() if not e["changed_choice"]]

    changed_sucess_rate = 100*sum(changed_and_won)/len(changed_and_won) if len(changed_and_won) > 0 else 0
    notchanged_success_rate = 100*sum(notchanged_and_won)/len(notchanged_and_won) if len(notchanged_and_won) > 0 else 0

    s1 = "Changed and won: {} out of {} ({}% success)".format(sum(changed_and_won), len(changed_and_won), changed_sucess_rate)
    s2 = "Not changed and won: {} out of {} ({}% success)".format(sum(notchanged_and_won), len(notchanged_and_won), notchanged_success_rate)
    return "<h1>Statistics</h1>{}</br>{}".format(s1, s2)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
