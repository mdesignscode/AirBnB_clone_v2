#!/usr/bin/python3
""" Amenity Module for HBNB project """
from models import storage_type
from models.base_model import (
    Base,
    BaseModel,
    Column,
    ForeignKey,
    relationship,
    VARCHAR)


class Amenity(BaseModel, Base):
    """Amenity class for HBNB project"""
    __tablename__ = 'amenities'
    place_amenities = relationship(
        'Place', secondary='place_amenity', backref='amenities')

    if storage_type == 'db':
        name = Column(VARCHAR(128), nullable=False)

    else:
        name = ""
