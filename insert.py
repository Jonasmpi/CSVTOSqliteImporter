from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import exists
from schema import Produkt,Base
import csv
import sys 
import codecs
engine = create_engine('sqlite:///sqlalchemy_sqllite.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

#new_products = Produkt(name="Test",preis=12.34,kategorie="Obst")
with open('data.csv', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile, delimiter=';')
    for row in reader:
        print(row[0])                
        name = row[1]        
        new_products = Produkt(name=name,preis=float(row[2]),kategorie=row[3])
        session.add(new_products)
    session.commit()
