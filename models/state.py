#!/usr/bin/python3
"""State class"""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String
import models
from models.base_model import BaseModel, Base
from models.city import City
import shlex


class State(BaseModel, Base):
    """State class"""

    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship("City", cascade='all, delete, delete-orphan',
                          backref="state")

    @property
    def cities(self):
        data = models.storage.all()
        locale = []
        result = []
        for key in data:
            city = key.replace('.', ' ')
            city = shlex.split(city)
            if (city[0] == 'City'):
                locale.append(data[key])
        for elem in locale:
            if (elem.state_id == self.id):
                result.append(elem)
        return (result)
