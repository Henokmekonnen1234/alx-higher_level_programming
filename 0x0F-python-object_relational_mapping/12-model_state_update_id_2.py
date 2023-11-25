#!/usr/bin/python3
"""
module 12-model_state_update_id_2.py

This module will change the name of the id=2 to "New mexico" into states
table using sqlalchemy
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
        result = session.query(State).filter_by(id=2).first()
        if result is not None:
            result.name = "New Mexico"
            session.commit()
        else:
            pass
    except Exception as e:
        pass
