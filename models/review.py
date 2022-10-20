#!/usr/bin/python3
""" Review module for the HBNB project """
from models import storage_type
from models.base_model import (
    Base,
    BaseModel,
    Column,
    ForeignKey,
    VARCHAR)


class Review(BaseModel, Base):
    """ Review class to store review information """
    __tablename__ = 'reviews'

    if storage_type == 'db':
        place_id = Column(VARCHAR(60),
                          ForeignKey('places.id',
                                     ondelete='CASCADE',
                                     onupdate='CASCADE'),
                          nullable=False)
        user_id = Column(VARCHAR(60),
                         ForeignKey('users.id',
                                    ondelete='CASCADE',
                                    onupdate='CASCADE'),
                         nullable=False)
        text = Column(VARCHAR(1024), nullable=False)

    else:
        place_id = ''
        user_id = ''
        text = ''
