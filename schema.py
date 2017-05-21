import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship,backref
from sqlalchemy import create_engine
from sqlalchemy.sql import func
from sqlalchemy import DateTime
Base = declarative_base()

#Schema constructed here
class Produkt(Base):
    __tablename__ = 'produkt'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    preis = Column(Float)
    kategorie = Column(String(50))

# Create an engine that stores data in the local directory's
# sqlalchemy_example.db file.
engine = create_engine('sqlite:///sqlalchemy_sqllite.db')
print("Engine created....")

# Create all tables in the engine. This is equivalent to "Create Table"
# statements in raw SQL.
Base.metadata.create_all(engine)
print("Create all tables done....")