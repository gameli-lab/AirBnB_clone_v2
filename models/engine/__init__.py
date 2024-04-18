#!/usr/bin/python3
import os

HBNB_TYPE_STORAGE = os.getenv('HBNB_TYPE_STORAGE')

if HBNB_TYPE_STORAGE == 'db':
    from .db_storage import DBStorage
    storage = DBStorage()
else:
    from .file_storage import FileStorage
    storage = FileStorage()

storage.reload()
