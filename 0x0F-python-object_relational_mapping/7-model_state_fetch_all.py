#!/usr/bin/python3
'''
Lists all State objects from the database hbtn_0e_6_usa
'''

from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sys

if __name__ == '__main__':
    # Create engine to connect to MySQL
    # server running on localhost port 3306'''
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)

    # Create all tables in the engine.
    # = "Create Table" in raw SQL.'''
    Base.metadata.create_all(engine)

    # Create a configured "Session" class
    Session = sessionmaker(bind=engine)

    # Create a Session
    session = Session()

    # Query all State objects
    for state in session.query(State).order_by(State.id):
        print("{}: {}".format(state.id, state.name))

    # Close session
    session.close()
