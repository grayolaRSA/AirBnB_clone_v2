#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, Table, ForeignKey
from sqlalchemy.orm import relationship


class Amenity(BaseModel, Base):
    """class for amenities"""

    __tablename__ = 'amenities'
    if models.storage_t == "db":
        name = Column(String(128), nullable=False)
        place_amenities = relationship("Place", secondary="place_amenity",
                                       backref="amenities",
                                       viewonly=False)
    else:
        name = ""
