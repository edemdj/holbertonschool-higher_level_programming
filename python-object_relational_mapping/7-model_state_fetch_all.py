#!/usr/bin/python3
"""script that lists all State objects from the database"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

def list_states(username, password, database):

    engine = create_engine(f"mysql://{username}:{password}@localhost:3306/{database}")

    Session = sessionmaker(bind=engine)
    session = Session()

    states = session.query(State).order_by(State.id).all()

    for state in states:
        print(f"{state.id}: {state.name}")
    session.close()

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python script.py <username> <password> <database>")
    else:
        username = sys.argv[1]
        password = sys.argv[2]
        database = sys.argv[3]
        list_states(username, password, database)
