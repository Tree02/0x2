import sqlalchemy

from sqlalchemy import Column, Integer, String
from sqlalchemy.sql import func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

from flask import jsonify

engine = sqlalchemy.create_engine("sqlite:///database.db")

base = declarative_base()

class Users(base):
    __tablename__ = "Postulantes"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    lastName = Column(String)
    email = Column(String)

    def __repr__(self):
        return self
    def jsonify(self):
        return ({
            'id' : self.id,
            'description' : self.description,
            'amount' : self.amount,
            'date' : self.date
        })

class Clients(base):
    __tablename__ = "Clientes"

    id = Column(Integer, primary_key=True, autoincrement=True)
    company = Column(String)
    representative = Column(String)
    email = Column(String)
    phone = Column(Integer)

    def __repr__(self):
        return self

def insertP(n, l, e):
    Session = sessionmaker(bind=engine)
    session = Session()

    a = Users(name=n, lastName=l, email=e)
    
    session.add(a)
    session.commit()

def insertC(c, r, e, p):
    Session = sessionmaker(bind=engine)
    session = Session()

    a = Clients(company=c, representative=r, email=e, phone=p)
    
    session.add(a)
    session.commit()

if __name__ == "__main__":
    base.metadata.create_all(engine)