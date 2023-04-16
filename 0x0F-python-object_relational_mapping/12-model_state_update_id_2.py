#!/usr/bin/python3

'''
script that changes the name of a State object from the database hbtn_0e_6_usa
'''

import sys
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.exc import NoResultFound

if __name__ == "__main__":
    # create engine
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    # create session
    Session = sessionmaker(bind=engine)
    session = Session()

    # query
    try:
        state = session.query(State).filter_by(id=2).one()
        state.name = "New Mexico"
        session.commit()
    except NoResultFound:
        pass

    session.close()
