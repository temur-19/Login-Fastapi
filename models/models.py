from dataclasses import Field

from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.ext.declarative import declarative_base
from db.db import Base
class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String)
    password = Column(String)

