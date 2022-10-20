#!/usr/bin/python3
"""starts a Flask web application"""

from flask import Flask, render_template
from models import storage
from models.amenity import Amenity
from models.city import City
from models.state import State
from models.engine.db_storage import DBStorage as db

app = Flask(__name__)


@app.teardown_appcontext
def close_session(session):
    """remove the current SQLAlchemy Session"""
    storage.close()


@app.route('/hbnb_filters', strict_slashes=False)
def show_cities():
    """displays a dynamic page"""

    session = db()._DBStorage__session
    return render_template('10-hbnb_filters.html',
                           states=storage.all(State).values(),
                           Amenity=Amenity,
                           City=City,
                           session=session)


app.run(port=5000, host='0.0.0.0')
