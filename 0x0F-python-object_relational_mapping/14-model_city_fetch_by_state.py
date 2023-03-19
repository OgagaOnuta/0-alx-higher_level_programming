#!/usr/bin/python3
'''Lists all data from a table in a database'''

import sys
from model_state import Base, State
from model_city import City

from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.
                           format(sys.argv[1], sys.argv[2],
                                  sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)

    session = Session()

    for state_name, city_id, city_name in \
        session.query(State.name, City.id, City.name)\
               .join(State).order_by(City.id).all():
        print("{}: ({}) {}".format(state_name, city_id, city_name))
