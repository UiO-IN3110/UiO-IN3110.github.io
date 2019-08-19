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
    game_id = str(uuid.uuid4())  # Create a unique identifier for this game
    winning = random.randint(1, 3)  # Define a winning door
    game_states[game_id] = winning

    return render_template('select4.html', game_id=game_id)

@app.route('/reselect', methods=['POST']) 
def reselect():           

    # request.form contains all form parameters, like the selected door
    selected = int(request.form["door"])
    
    # request.args contains the URL parameters, like the game_id
    game_id = request.args.get("game_id")
    winning = game_states[game_id]

    # Open a random door (but not the winning nor the user-chosen door)
    opened = set([1, 2, 3])
    opened.discard(winning)
    opened.discard(selected)
    opened = random.choice(list(opened))

    return render_template("reselect4.html", game_id=game_id, selected=selected, opened=opened)

if __name__ == "__main__":
    app.run(debug=True)
