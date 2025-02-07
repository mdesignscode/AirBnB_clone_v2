#!/usr/bin/python3
"""starts a Flask web application"""

from flask import Flask


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """display “Hello HBNB!”"""
    return 'Hello HBNB!'


app.run(port=5000, host='0.0.0.0')
