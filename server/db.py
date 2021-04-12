#!/usr/bin/python3

from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, TIMESTAMP, func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy import text


Base = declarative_base()


class User(Base):
    __tablename__ = "person"

    id = Column('id', Integer, primary_key=True, autoincrement=True)
    username = Column('username', String, unique=True)
    last_login_date = Column(TIMESTAMP(timezone=False), server_default=func.now(), nullable=False)


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



users = session.query(User).all()

for user in users:
    print(f"The username is {user.username} and id: {user.id} and they last logged in at: {user.last_login_date}")

session.close()
