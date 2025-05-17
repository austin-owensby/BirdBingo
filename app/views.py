from . import app
from flask import render_template

@app.route("/")
def app():
    return render_template("app.html")