#!/usr/bin/python3
""" script that lists all State objects that contain the letter a"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

def print_first_state(username, password, database):
    engine = create_engine(f"mysql://{username}:{password}@localhost:3306/{database}")

    Session = sessionmaker(bind=engine)
    session = Session()

    first_state = session.query(State).order_by(State.id).first()

    if first_state:
        print(f"{first_state.id}: {first_state.name}")
    else:
        print("Nothing")
    session.close()

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python script.py <username> <password> <database>")
    else:
        from model_state import Base, State
        username = sys.argv[1]
        password = sys.argv[2]
        database = sys.argv[3]
        print_first_state(username, password, database)
