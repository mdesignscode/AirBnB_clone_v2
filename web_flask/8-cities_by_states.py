#!/usr/bin/python3
"""starts a Flask web application"""

from flask import Flask, render_template
from sqlalchemy import text
from models import storage, storage_type
from models.city import City
from models.state import State
from models.engine.db_storage import DBStorage as db

app = Flask(__name__)


@app.teardown_appcontext
def close_session(session):
    """remove the current SQLAlchemy Session"""
    storage.close()


@app.route('/cities_by_states', strict_slashes=False)
def list_states():
    """lists all cities linked to a state"""

    session = db()._DBStorage__session
    return render_template('8-cities_by_states.html',
                           states=storage.all(State),
                           City=City,
                           storage_type=storage_type,
                           session=session)


app.run(port=5000, host='0.0.0.0')
