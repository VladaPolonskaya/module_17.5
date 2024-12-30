from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase
from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import Session

engine = create_engine("sqlite:///taskmanager.db", echo = True)

SessionLocal = sessionmaker(bind=engine)


class Base(DeclarativeBase):
    pass