#!/usr/bin/python3
""" City Module for HBNB project """
import models
from models.base_model import BaseModel
from models.base_model import Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship


class City(BaseModel, Base):
    """ The city class, contains state ID and name """
    from models.place import Place

    __tablename__ = 'cities'

    if models.storage_t == "db":
        id = Column(String(60), primary_key=True, nullable=False)
        name = Column(String(128), nullable=False)
        state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
        places = relationship("Place", cascade="all, delete", backref="city")
    else:
        name = ''
        state_id = ''
