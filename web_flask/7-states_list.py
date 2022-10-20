#!/usr/bin/python3
"""starts a Flask web application"""

from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.teardown_appcontext
def close_session(session):
    """remove the current SQLAlchemy Session"""
    storage.close()


@app.route('/states_list', strict_slashes=False)
def list_states():
    """lists all states"""
    return render_template('7-states_list.html', states=storage.all(State))


app.run(port=5000, host='0.0.0.0')
