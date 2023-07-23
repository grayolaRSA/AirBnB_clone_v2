#!/usr/bin/python3
"""
Module for creation of new engine
"""
import models
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from os import getenv
from models.base_model import Base


class DBStorage:
    """Database storage class"""
    __engine = None
    __session = None

    def __init__(self):
        """create an DB storage object"""
        HBNB_MYSQL_USER = getenv('HBNB_MYSQL_USER')
        HBNB_MYSQL_PWD = getenv('HBNB_MYSQL_PWD')
        HBNB_MYSQL_HOST = getenv('HBNB_MYSQL_HOST')
        HBNB_MYSQL_DB = getenv('HBNB_MYSQL_DB')
        HBNB_ENV = getenv('HBNB_ENV')
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.
                           format(HBNB_MYSQL_USER, HBNB_MYSQL_PWD,
                                  HBNB_MYSQL_HOST, HBNB_MYSQL_DB),
                           pool_pre_ping=True)

        if HBNB_ENV == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """query on the current database session"""
        new_dict = {}
        if cls:
            for clss in classes.values():
                if issubclass(cls, clss):
                    objs = self.__session.query(clss).all()
                    for obj in objs:
                        key = obj.__class__.__name__ + '.' + obj.id
                        new_dict[key] = obj
        else:
            for clss in classes.values():
                objs = self.__session.query(clss).all()
                for obj in objs:
                    key = obj.__class__.__name__ + '.' + obj.id
                    new_dict[key] = obj
        return (new_dict)

    def new(self, obj):
        """add the object to the current database session"""
        self.__session.add(obj)

    def save(self):
        """commit all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """delete from the current database session obj if not None"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """reloads data from the database"""
        from models.user import User
        from models.place import Place
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review

        classes = {"Amenity": Amenity, "City": City, "Place": Place,
                   "Review": Review, "State": State, "User": User}


        Base.metadata.create_all(self.__engine)
        sess_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(sess_factory)
        self.__session = Session

    def close(self):
        """call remove() method on the private session attribute"""
        self.__session.remove()
