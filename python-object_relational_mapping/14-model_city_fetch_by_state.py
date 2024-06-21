#!/usr/bin/python3
"""script that changes the name of a State object"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

def change_state_name(username, password, database):
    engine = create_engine(f"mysql://{username}:{password}@localhost:3306/{database}")

    Session = sessionmaker(bind=engine)
    session = Session()

    state_to_change = session.query(State).filter_by(id=2).first()
    if state_to_change:
        state_to_change.name = "New Mexico"
        session.commit()
    else:
        print("State with id=2 not found")
    session.close()

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python script.py <username> <password> <database>")
    else:
        from model_state import Base, State
        username = sys.argv[1]
        password = sys.argv[2]
        database = sys.argv[3]
        change_state_name(username, password, database)
