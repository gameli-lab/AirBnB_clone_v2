#!/usr/bin/python3
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
import os

class DBStorage:
    __engine = None
    __session = None

    def __init__(self):
        self.__engine = create_engine(
            'mysql+mysqldb://{}:{}@{}/{}'.format(
                os.getenv('HBNB_MYSQL_USER'),
                os.getenv('HBNB_MYSQL_PWD'),
                os.getenv('HBNB_MYSQL_HOST'),
                os.getenv('HBNB_MYSQL_DB')),
            pool_pre_ping=True)

        if os.getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        new_dict = {}
        if cls is None:
            classes = ['User', 'State', 'City', 'Amenity', 'Place', 'Review']
            for class_name in classes:
                objs = self.__session.query(eval(class_name)).all()
                for obj in objs:
                    key = "{}.{}".format(type(obj).__name__, obj.id)
                    new_dict[key] = obj
        else:
            objs = self.__session.query(cls).all()
            for obj in objs:
                key = "{}.{}".format(type(obj).__name__, obj.id)
                new_dict[key] = obj
        return new_dict

    def new(self, obj):
        self.__session.add(obj)

    def save(self):
        self.__session.commit()

    def delete(self, obj=None):
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(
            bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session
