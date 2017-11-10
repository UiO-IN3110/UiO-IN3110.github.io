"""
A Basic Monty Hall Game.
========================

Run with
python game_server2.py


Improvements to game_server1.py:
- /select URL implemented and and rendered from a template. 
- The template contains a form with a POST request to the /reselect.
"""


from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/")
def root():
    return """<h1>Welcome to the <b>magic door</b> game!</h1>
<a href="/select/">Launch game</a>
"""

@app.route("/select/")
def new():
    return render_template('select2.html')

if __name__ == "__main__":
    app.run(debug=True)
