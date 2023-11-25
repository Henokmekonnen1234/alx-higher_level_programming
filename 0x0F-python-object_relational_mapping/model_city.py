#!/usr/bin/python4
"""
module model_city.py

This module will create city table using sqlalchemy
"""

from model_state import Base, Session
from sqlalchemy import create_engine, Integer, String, ForeignKey
from sqlalchemy import Sequence, Column
from sqlalchemy.orm import relationship


class City(Base):
    """this will create the city table"""
    __tablename__ = "cities"
    id = Column(Integer, Sequence("cities_id_seq"), primary_key=True,
                unique=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
    states = relationship("State", back_populates="cities")

    def __init__(self, name=None, state_id=None):
        """this will initializes the column name and state_id"""
        if name is not None and state_id is not None:
            self.name = name
            self.state_id = state_id
