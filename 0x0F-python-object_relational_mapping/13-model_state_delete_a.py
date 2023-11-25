#!/usr/bin/python3
"""
module 13-model_state_delete_a.py

This module will delete name which contain letter 'a' in states
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
        delete_name = State.__table__.delete().where(State.name.like("%a%"))
        if delete_name is not None:
            session.execute(delete_name)
            session.commit()
        else:
            pass
    except Exception as e:
        pass
