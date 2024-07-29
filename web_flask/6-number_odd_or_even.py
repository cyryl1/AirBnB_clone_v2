#!/usr/bin/python3
"""
A simple Flask web application
"""

from flask import Flask, render_template

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


@app.route("/number/<int:n>", strict_slashes=False)
def integer(n):
    """
    display “Python ”, followed by the value of the text variable
    (replace underscore _ symbols with a space )
    """
    return "{} is a number".format(n)


@app.route("/number_template/<int:n>", strict_slashes=False)
def number_template(n):
    """
    Display an HTML page only if n is an integer.
    """
    return render_template('5-number.html', n=n)


@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def number_odd_or_even(n):
    """
    Display an HTML pagee only if n is an intger
    """
    return render_template('6-number_odd_or_even.html', n=n)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
