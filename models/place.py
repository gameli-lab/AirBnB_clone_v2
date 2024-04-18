#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, Float, ForeignKey, Table
from sqlalchemy.orm import relationship

# Create a new table for the many-to-many relationship
place_amenity = Table(
    'place_amenity', Base.metadata,
    Column('place_id', String(60), ForeignKey('places.id'),
           primary_key=True, nullable=False),
    Column('amenity_id', String(60), ForeignKey('amenities.id'),
           primary_key=True, nullable=False)
)

class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = 'places'
    # ... other attributes ...

    amenities = relationship("Amenity", secondary=place_amenity,
                             viewonly=False)

    @property
    def amenities(self):
        """getter attribute that returns the list of Amenity instances
        based on the attribute amenity_ids that contains all Amenity.id
        linked to the Place"""
        from models import storage
        return [amenity for amenity in storage.all(Amenity).values()
                if amenity.id in self.amenity_ids]

    @amenities.setter
    def amenities(self, obj):
        """setter attribute that handles append method for adding an
        Amenity.id to the attribute amenity_ids. This method should
        accept only Amenity object, otherwise, do nothing."""
        if isinstance(obj, Amenity):
            self.amenity_ids.append(obj.id)
