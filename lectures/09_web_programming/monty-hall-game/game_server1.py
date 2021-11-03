"""
A Basic Monty Hall Game.
========================

Run with
python game_server1.py
"""

from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()


@app.get("/", response_class=HTMLResponse)
def root():
    return """<h1>Welcome to the <b>magic door</b> game!</h1>
<a href="/select">Launch game</a>
"""


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app)
