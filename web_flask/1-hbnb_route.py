#!/usr/bin/python3
""" Model Route Flask v0.00.0 """
from flask import Flask


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """Route page"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def index():
    """ /hbnb route """
    return 'HBNB'


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
