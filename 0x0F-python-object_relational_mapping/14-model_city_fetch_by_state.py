#!/usr/bin/python3
"""
module  14-model_city_fetch_by_state.py

This module will delete name which contain letter 'a' in states
table using sqlalchemy
"""

if __name__ == "__main__":
    from model_state import Base, State
    from model_city import City
    from sqlalchemy.orm import Session
    from sqlalchemy import create_engine
    import sys

    try:
        engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}".
                               format(sys.argv[1], sys.argv[2],
                                      sys.argv[3]), pool_pre_ping=True)
        Base.metadata.create_all(engine)
        session = Session(engine)
        session.commit()
        result = session.query(State).join(State.cities)\
            .order_by(City.id).all()
        if result is not None:
            for value in result:
                for city in value.cities:
                    print("{}: ({}) {} ".format(value.name,
                                                city.id, city.name))
    except Exception as e:
        print(e)
