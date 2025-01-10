from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import declarative_base
from datetime import datetime

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    birth = Column(DateTime, nullable=False)
    created = Column(DateTime, default=datetime.now)
    fav_food = Column(String, nullable=False)

    def __repr__(self):
        return f'{self.name} nasceu em [{self.birth}] e gosta de ao mossar {self.fav_food}'