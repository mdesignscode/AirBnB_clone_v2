#!/usr/bin/python3
""" Place Module for HBNB project """
from models import storage, storage_type
from models.base_model import (
    Base,
    BaseModel,
    Column,
    Float,
    ForeignKey,
    INT,
    relationship,
    Table,
    VARCHAR)
from models.review import Review


place_amenity = Table(
    "place_amenity",
    Base.metadata,
    Column('place_id', VARCHAR(60), ForeignKey(
        'places.id', onupdate='CASCADE',
        ondelete='CASCADE'), primary_key=True),
    Column('amenities_id', VARCHAR(60), ForeignKey(
        'amenities.id', onupdate='CASCADE',
        ondelete='CASCADE'), primary_key=True)
)


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = 'places'

    if storage_type == 'db':
        user_id = Column(VARCHAR(60),
                         ForeignKey('users.id',
                                    ondelete='CASCADE',
                                    onupdate='CASCADE'),
                         nullable=False)
        city_id = Column(VARCHAR(60),
                         ForeignKey('cities.id',
                                    ondelete='CASCADE',
                                    onupdate='CASCADE'),
                         nullable=False)
        name = Column(VARCHAR(128), nullable=False)
        description = Column(VARCHAR(1024))
        number_rooms = Column(INT, server_default='0', nullable=False)
        number_bathrooms = Column(INT, server_default='0', nullable=False)
        max_guest = Column(INT, server_default='0', nullable=False)
        price_by_night = Column(INT, server_default='0', nullable=False)
        latitude = Column(Float)
        longitude = Column(Float)
        reviews = relationship('Review',
                               cascade="all, delete-orphan",
                               post_update=True)

        amenities = relationship(
            "Amenity", secondary='place_amenity', viewonly=False,
            back_populates="places")

    else:
        city_id = ""
        user_id = ""
        name = ""
        description = ""
        number_rooms = 0
        number_bathrooms = 0
        max_guest = 0
        price_by_night = 0
        latitude = 0.0
        longitude = 0.0
        amenity_ids = []

    @property
    def reviews(self):
        """returns the list of Review instances with place_id
        equals to the current Place.id"""

        all_reviews = storage.all(Review)
        reviews_list = []
        for review in all_reviews.values():
            if review.place_id == self.id:
                reviews_list.append(review)

        return reviews_list

    @property
    def amenities(self):
        """returns the list of Amenity instances based on the attribute
        amenity_ids that contains all Amenity.id linked to the Place"""
        from amenity import Amenity
        amenities = []
        for id in self.amenity_ids:
            id_dict = storage.all()[f'Amenity.{id}']
            model = Amenity(**id_dict)
            amenities.append(model)
        return amenities

    @amenities.setter
    def amenities(self, amenity):
        """adds an amenity id to the list"""
        from amenity import Amenity
        if isinstance(amenity, Amenity):
            self.amenity_ids.append(amenity)
