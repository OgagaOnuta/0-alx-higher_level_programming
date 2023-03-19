#!/usr/bin/python3
'''Implements the deprecated get() function'''

import sys
from model_state import Base, State

from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.
                           format(sys.argv[1], sys.argv[2],
                                  sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)

    session = Session()

    state_id_list = []
    state_name_list = []
    for state in session.query(State).all():
        state_id_list.append(state.id)
        state_name_list.append(state.name)

    state = sys.argv[4]
    if (state not in state_name_list):
        print("Not found")
    else:
        index = state_name_list.index(state)
        print(state_id_list[index])
