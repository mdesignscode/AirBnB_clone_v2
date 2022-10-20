#!/usr/bin/python3
"""starts a Flask web application"""

from flask import Flask, escape


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """display “Hello HBNB!”"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """display HBNB"""
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c_variable(text):
    """display display “C ” followed by the value of the text variable"""
    return f"C {escape(text).replace('_', ' ')}"


@app.route('/python/', defaults={'text': 'is cool'})
@app.route('/python/<text>', strict_slashes=False)
def python_variable(text):
    """display display “Python ” followed by the value of the text variable"""
    return f"Python {escape(text).replace('_', ' ')}"


@app.route('/number/<int:n>', strict_slashes=False)
def is_int(n):
    """display “n is a number” only if n is an integer"""
    if type(n) is int:
        return f"{n} is a number"


app.run(port=5000, host='0.0.0.0')
