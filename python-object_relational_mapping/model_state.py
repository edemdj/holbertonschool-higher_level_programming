#!/usr/bin/python3
"""class definition of a State and an instance"""
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class State(Base):
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)


if __name__ == "__main__":
    engine = create_engine('mysql://username:password@localhost:3306/database_name')
    Base.metadata.create_all(engine)
