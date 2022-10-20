#!/usr/bin/python3
""" State Module for HBNB project """
from models import storage, storage_type
from models.base_model import Base, BaseModel, Column, VARCHAR
from sqlalchemy.orm import relationship

from models.city import City


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'

    if storage_type == 'db':
        name = Column(VARCHAR(128), nullable=False)
        cities = relationship("City",
                              cascade="all, delete-orphan",
                              post_update=True)

    else:
        name = ''

    @property
    def cities(self):
        """retrieves all the cities of the current state"""

        all_cities = storage.all(City)
        cities_list = []
        for city in all_cities.values():
            if city.state_id == self.id:
                cities_list.append(city)

        return cities_list
