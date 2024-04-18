#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Table
from sqlalchemy.orm import relationship
from sqlalchemy import ForeignKey

# This table represents the many-to-many relationship between Place and Amenity
place_amenity = Table(
    'place_amenity', Base.metadata,
    Column('place_id', String(60), ForeignKey('places.id'),
           primary_key=True, nullable=False),
    Column('amenity_id', String(60), ForeignKey('amenities.id'),
           primary_key=True, nullable=False)
)

# The Amenity class inherits from both BaseModel and Base
# It represents an amenity in the HBNB project
class Amenity(BaseModel, Base):
    """Amenity class for HBNB project"""
    __tablename__ = 'amenities'  # Represents the table name
    name = Column(String(128), nullable=False)  # Represents a column containing a string (128 characters), can’t be null
    # Represents a relationship Many-To-Many between the class Place and Amenity
    place_amenities = relationship(
        "Place", secondary=place_amenity, viewonly=True
    )
