#!/usr/bin/python3
"""This module defines a class User"""
from models import storage_type
from models.base_model import (
    BaseModel,
    Base,
    Column,
    relationship,
    VARCHAR)


class User(BaseModel, Base):
    """This class defines a user by various attributes"""
    __tablename__ = 'users'

    if storage_type == 'db':
        email = Column(VARCHAR(128), nullable=False)
        password = Column(VARCHAR(128), nullable=False)
        first_name = Column(VARCHAR(128))
        last_name = Column(VARCHAR(128))
        places = relationship('Place',
                              cascade="all, delete-orphan",
                              post_update=True)
        reviews = relationship('Review',
                               cascade="all, delete-orphan",
                               post_update=True)

    else:
        email = ''
        password = ''
        first_name = ''
        last_name = ''
