import sqlalchemy as sa
from sqlalchemy.orm import sessionmaker
import datetime
from model.models import User

db = sa.create_engine("sqlite:///cupid.db")
session_maker = sessionmaker(bind=db)

template_users = [
    User(name="Amora",birth=datetime.datetime(2001,10,8),created=datetime.datetime.now(),fav_food="ao mosso"),
    User(name="PORRA",birth=datetime.datetime(2044,4,20),created=datetime.datetime.now(),fav_food="mamae")
]

def create_template_users()->None:
    with session_maker() as session:
        for user in template_users:
            session.add(user)
        session.commit()

def get_all_users()->list[User]:
    with session_maker() as session:
        all_users = session.query(User).all()
        for user in all_users:
            print("Fetched user:")
            print(user)

        return all_users