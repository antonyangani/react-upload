#!/usr/bin/python3

from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship


Base = declarative_base()


class User(Base):
    __tablename__ = "person"

    id = Column('id', Integer, primary_key=True)
    username = Column('username', String, unique=True)


engine = create_engine('sqlite:///users.db', echo=True)
Base.metadata.create_all(bind=engine)
Session = sessionmaker(bind=engine)

# Creating a session object to help in creating, updating, deleting objects in database

session = Session()

# Adding user

# user = User()
# user.id = 1
# user.username = "Anthony"
# session.add(user)
# session.commit()

users = session.query(person).all()

