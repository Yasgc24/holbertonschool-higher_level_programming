#!/usr/bin/python3
"""script 14-model_city_fetch_by_state.py that
prints all City objects from the database hbtn_0e_14_usa"""

from unicodedata import name


if __name__ == "__main__":

    from sys import argv
    from relationship_state import Base, State
    from relationship_city import City
    from sqlalchemy import create_engine
    from sqlalchemy.orm import Session
    from sqlalchemy.schema import Table


    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    session = Session(engine)
    new_city = City(name='San Francisco')
    new_state = State(name='California')
    new_state.cities.append(new_city)
    session.add_all([new_state, new_city])
    session.commit()
    session.close()
