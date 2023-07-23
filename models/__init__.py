#!/usr/bin/python3
"""This module instantiates file or db storage depending on env variable"""

from os import getenv

storage_t = getenv("HBNB_TYPE_STORAGE")

def init_storage():
    """initialise the storage based on the environment variable"""

    if storage_t == "db":
        from models.engine.db_storage import DBStorage
        storage = DBStorage()
    else:
        from models.engine.file_storage import FileStorage
        storage = FileStorage()

storage = init_storage()
storage.reload()
