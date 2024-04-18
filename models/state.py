#!/usr/bin/python3
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state", cascade="all, delete")

    @property
    def cities(self):
        """Get City instances with state_id equals to the current State.id"""
        from models import storage
        return [city for city in storage.all(City).values()
                if city.state_id == self.id]
