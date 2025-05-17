from flask import Flask
import os

app = Flask(__name__)

DATABASE_URL = os.getenv("DATABASE_URL")

if DATABASE_URL is None:
    # If developing locally, follow the README to add it
    raise Exception("Could not find a DATABASE_URL environmental variable.")

@app.route("/")
def hello_world():
    return "<p>Hello, World</p>"