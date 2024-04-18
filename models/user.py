#!/usr/bin/python3
"""
This module defines the User and Place classes using SQLAlchemy.
"""

from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base


class User(BaseModel, Base):
    """
    This class defines a user by various attributes.
    Each user can have multiple places and reviews associated with it.
    """

    __tablename__ = 'users'
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128), nullable=True)
    last_name = Column(String(128), nullable=True)
    places = relationship(
        "Place", backref="user", cascade="all, delete-orphan"
    )
    reviews = relationship(
        "Review", backref="user", cascade="all, delete-orphan"
    )


class Place(BaseModel, Base):
    """
    This class defines a place by various attributes.
    Each place is associated with a user.
    """

    __tablename__ = 'places'
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
