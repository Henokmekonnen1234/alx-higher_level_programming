#!/usr/bin/python3
"""
module 7-model_state_fetch_all.py

This module will fetch all states table data using sqlalchemy
"""

from model_state import Base, State, Session
from sqlalchemy import create_engine
import sys

if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}".
                           format(sys.argv[1], sys.argv[2],
                                  sys.argv[3]), pool_pre_ping=True)
    try:
        Base.metadata.create_all(engine)
        session = Session()
        result = session.query(State).all()
        for value in result:
            print("{}: {}".format(value.id, value.name))
    except Exception as e:
        print("{}".format(e))
