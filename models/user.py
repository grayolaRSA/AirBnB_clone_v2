#!/usr/bin/python3
"""This module defines a class User"""
from models.base_model import BaseModel, Base
import sqlalchemy
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship


class User(BaseModel, Base):
    """This class defines a user by various attributes"""
    __tablename__ = 'users'
    if models.storage_t = "db":
        email = Column(String(128), nullable=False)
        password = Column(String(128), nullable=False)
        first_name = Column(String(128))
        last_name = Column(String(128))
        places = relationship("Place", cascade="all, delete", backref="user")
        review = relationship("Review", cascade="all, delete", backref="user")
    else:
        email = ''
        password = ''
        first_name = ''
        last_name = ''
