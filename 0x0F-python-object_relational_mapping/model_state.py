#!/usr/bin/python3
"""
module model_state.py

This module will CRUD data using sqlalchemy
"""

from sqlalchemy import create_engine, Column, Integer, String, Sequence
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import sys


try:
    engine = create_engine("mysql://{}:{}@localhost:3306/{}".
                           format(sys.argv[1], sys.argv[2],
                                  sys.argv[3]))
    Base = declarative_base()

    class State(Base):
        """This class will create the table states"""
        __tablename__ = "states"
        id = Column(Integer, Sequence("states_id_seq"),
                    primary_key=True, unique=True, nullable=False)
        name = Column(String(128), nullable=False)

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()
    session.commit()
except Exception as e:
    print(e)
