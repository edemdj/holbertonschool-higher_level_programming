#!/usr/bin/python3
"""Script that deletes all State objects with a name containing the letter a"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City  # Import City model here

def delete_states_with_letter_a(username, password, database):
    try:
        engine = create_engine(f"mysql://{username}:{password}@localhost:3306/{database}")

        Base.metadata.create_all(engine)

        Session = sessionmaker(bind=engine)
        session = Session()

        states_with_a = session.query(State).filter(State.name.like('%a%')).all()

        for state in states_with_a:
            session.delete(state)
        
        session.commit()
        print("States with names containing 'a' deleted successfully.")

    except Exception as e:
        print(f"An error occurred: {e}")
        if session:
            session.rollback()  # Rollback changes in case of error

    finally:
        if session:
            session.close()

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python script.py <username> <password> <database>")
    else:
        username = sys.argv[1]
        password = sys.argv[2]
        database = sys.argv[3]

        delete_states_with_letter_a(username, password, database)
