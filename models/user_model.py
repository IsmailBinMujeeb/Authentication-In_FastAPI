from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = "Users"

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String(15))
    last_name = Column(String(15))
    username = Column(String(20), unique=True, index=True)
    email = Column(String(50), unique=True)
    password = Column(String(100))