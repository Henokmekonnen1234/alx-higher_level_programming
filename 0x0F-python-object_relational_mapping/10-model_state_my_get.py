#!/usr/bin/python3
"""
module 10-model_state_my_get.py

This module will fetch all states table data using sqlalchemy
"""

from model_state import Base, State, Session
from sqlalchemy import create_engine
import sys

if __name__ == "__main__":
    try:
        engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}".
                               format(sys.argv[1], sys.argv[2],
                                      sys.argv[3]), pool_pre_ping=True)
        Base.metadata.create_all(engine)
        session = Session()
        result = session.query(State).filter_by(name=sys.argv[4]).first()
        if result is not None:
            print("{}".format(result.id))
        else:
            print("{}".format("Not found"))
    except Exception as e:
        pass
