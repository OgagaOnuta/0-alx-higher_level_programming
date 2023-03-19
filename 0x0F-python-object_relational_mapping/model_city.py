#!/usr/bin/python3
'''Creates class definition of City'''

from model_state import Base, State

from sqlalchemy import (ForeignKey)
from sqlalchemy import (Column,
                        Integer,
                        String)


class City(Base):
    '''Class definition of City'''
    __tablename__ = 'cities'

    id = Column(Integer, autoincrement=True,
                unique=True, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
