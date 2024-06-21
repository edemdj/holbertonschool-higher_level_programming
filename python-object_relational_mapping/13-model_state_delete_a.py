#!/usr/bin/python3
"""script that deletes all State objects with a name containing the letter a"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

def delete_states_with_letter_a(username, password, database):
    engine = create_engine(f"mysql://{username}:{password}@localhost:3306/{database}")

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    states_with_a = session.query(State).filter(State.name.like('%a%')).all()

    for state in states_with_a:
        session.delete(state)
    session.commit()

    session.close()

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python script.py <username> <password> <database>")
    else:
        from model_state import Base, State
        username = sys.argv[1]
        password = sys.argv[2]
        Base
