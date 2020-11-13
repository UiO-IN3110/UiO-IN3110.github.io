from flask import Flask, render_template
from plots import norway_plot
import tempfile

app = Flask(__name__)

@app.route('/norway_plot')
def norway_plot_html():
    return render_template("norway_plot.html")

@app.route('/norway_plot.json')
def norway_plot_json():
    fig = norway_plot()

    tmp = tempfile.NamedTemporaryFile(suffix=".json")
    fig.save(tmp.name)
    
    with open(tmp.name) as file:
        return file.read()

app.run()
