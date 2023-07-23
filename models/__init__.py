#!/usr/bin/python3
"""
initialize the models package
"""

from os import getenv

def init_storage():
    """Initialize the storage based on the environment variable"""
    storage_t = getenv("HBNB_TYPE_STORAGE")

    if storage_t == "db":
        from models.engine.db_storage import DBStorage
        return DBStorage()
    else:
        from models.engine.file_storage import FileStorage
        return FileStorage()

storage = init_storage()
storage.reload()
