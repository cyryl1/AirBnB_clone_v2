#!/usr/bin/python3
"""
A simple Flask web application
"""

from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    """
    displays “Hello HBNB!” in the root route
    """
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """
    displays "HBNB" in the root console
    """
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c_text(text):
    """
    display “C ”, followed by the value of the text variable
    (replace underscore _ symbols with a space )
    """
    word = text.replace("_", " ")
    return "C {}".format(word)


@app.route("/python", defaults={"text": "is cool"}, strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python_text(text):
    """
    display “C ”, followed by the value of the text variable
    (replace underscore _ symbols with a space )
    """
    word = text.replace("_", " ")
    return "Python {}".format(word)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
