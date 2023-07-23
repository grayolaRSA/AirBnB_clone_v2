#!/usr/bin/python3
""" User Module for HBNB project """
import models
from os import getenv
from models.base_model import BaseModel, Base
import sqlalchemy
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship


class User(BaseModel, Base):
    """class for users"""

    __tablename__ = 'users'
    if models.storage_t == "db":
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128), nullable=True)
    last_name = Column(String(128), nullable=True)
    places = relationship("Place", cascade="all, delete-orphan",
                              backref="user")
    reviews = relationship("Review", cascade="all, delete-orphan",
                          backref="user")
    else:
        email = ""
        password = ""
        first_name = ""
        last_name = ""

    def __init__(self, *args, **kwargs):
        """initializes user"""
        super().__init__(*args, **kwargs)
