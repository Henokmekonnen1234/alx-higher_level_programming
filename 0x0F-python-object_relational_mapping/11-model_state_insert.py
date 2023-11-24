#!/usr/bin/python3
"""
module 11-model_state_insert.py

This module will add "Lousiana into states table using sqlalchemy
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
        new_state = State("Louisiana")
        session.add(new_state)
        session.commit()
        result = session.query(State).order_by(State.id.desc()).first()
        if result is not None:
            print("{}".format(result.id))
        else:
            print("{}".format("Not found"))
    except Exception as e:
        pass
