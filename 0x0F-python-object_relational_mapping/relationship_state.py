#!/usr/bin/python3
'''
class definition of a State and an instance Base = declarative_base()
'''

from sqlalchemy import Column, Integer, String, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

mymdata = MetaData()
Base = declarative_base(metadata=mymdata)


class State(Base):
    '''
    Class with id and name of each state
    '''
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, nullable=False,
                unique=True)
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state", cascade="all, delete")