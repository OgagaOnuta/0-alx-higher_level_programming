#!/usr/bin/python3
'''Lists all data in related tables in a database'''

import sys
from relationship_state import Base, State
from relationship_city import City

from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.
                           format(sys.argv[1], sys.argv[2],
                                  sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)

    session = Session()

    for state in session.query(State)\
                        .join(City)\
                        .order_by(City.id).all():
        for city in state.cities:
            print("{}: {} -> {}".format(city.id, city.name, state.name))
