#!/usr/bin/python3
"""that prints all City objects"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City

def fetch_cities_by_state(username, password, database):
    engine = create_engine(f"mysql://{username}:{password}@localhost:3306/{database}")

    Session = sessionmaker(bind=engine)
    session = Session()
    cities = session.query(City).order_by(City.id).all()

    for city in cities:
        print(f"{city.state.name}: ({city.id}) {city.name}")

    session.close()

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python script.py <username> <password> <database>")
    else:
        from model_city import Base, City
        username = sys.argv[1]
        password = sys.argv[2]
        database = sys.argv[3]
        fetch_cities_by_state(username, password, database)
