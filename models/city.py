#!/usr/bin/python3
""" City Module for HBNB project """
from models import storage_type
from models.base_model import (
    Base,
    BaseModel,
    Column,
    ForeignKey,
    relationship,
    VARCHAR)


class City(BaseModel, Base):
    """ The city class, contains state ID and name"""

    __tablename__ = 'cities'

    if storage_type == 'db':
        name = Column(VARCHAR(128), nullable=False)
        state_id = Column(VARCHAR(60),
                          ForeignKey('states.id',
                                     ondelete='CASCADE',
                                     onupdate='CASCADE'),
                          nullable=False)
        places = relationship('Place',
                              cascade="all, delete-orphan",
                              post_update=True)

    else:
        name = ""
        state_id = ""
