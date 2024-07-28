#!/usr/bin/python3

from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello():
    """
    This prints out the expression below
    """
    return "Hello HBNB!"


if __name__ == '__main__':
    # Ensure the app listens on host '0.0.0.0' and port '5000'
    app.run(host='0.0.0.0', port=5000, debug=False)
