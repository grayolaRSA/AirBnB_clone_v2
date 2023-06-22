#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, ForeignKey


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = 'places'
    if models.storage_t = "db":
        city_id = Column(String(60), nullable=False, ForeignKey('cities.id'))
        user_id = Column(String(60), nullable=False. ForeignKey('users.id'))
        name = Column(String(128), nullable=False)
        description = Column(String(1024), nullable=False)
        number_rooms = Column(int, nullable=False, default=0)
        number_bathrooms = Column(int, nullable=False, default=0)
        max_guest = Column(int, nullable=False, default=0)
        price_by_night = Column(int, nullable=False, default=0)
        latitude = Column(float, nullable=False)
        longitude = Column(float, nullable=False)
        reviews = relationship("Review", cascade="all, delete",
                               backref="place")
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
        @setter
        def reviews(self)
        "getter for list of instances related to the place"
        places_list = []
        all_places = models.storage.all(Place)
        for places in all_places.values():
            if places.place_id = self.id:
                places_list.append(places)
                return places_list
