"""
A Basic Monty Hall Game.
========================

Run with
python game_server1.py
"""

from flask import Flask

app = Flask(__name__)

@app.route("/")
def root():
    return """<h1>Welcome to the <b>magic door</b> game!</h1>
<a href="/select/">Launch game</a>
"""

if __name__ == "__main__":
    app.run(debug=True)
