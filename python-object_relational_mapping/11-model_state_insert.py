#!/usr/bin/python3
"""script that adds the State object “Louisiana” """
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

def add_state(username, password, database, new_state_name):
    engine = create_engine(f"mysql://{username}:{password}@localhost:3306/{database}")

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()
    new_state = State(name=new_state_name)

    session.add(new_state)

    session.commit()
    print(new_state.id)

    session.close()

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python script.py <username> <password> <database>")
    else:
        from model_state import Base, State
        username = sys.argv[1]
        password = sys.argv[2]
        database = sys.argv[3]
        add_state(username, password, database, "New State")