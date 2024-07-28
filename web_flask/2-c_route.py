#!/usr/bin/python3
"""
A simple flask project
"""

from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    """
    Displays "Hello HBNB!" on the root route"
    """
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """
    Displays "HBNB!" on the root route"
    """
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def text(text):
    """
    display “C ” followed by the value of the text variable
    (replace underscore _ symbols with a space )
    """
    word = text.replace("_", " ")
    return "C {}".format(word)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
