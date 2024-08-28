from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from decouple import config

SQLALCHEMY_DATABASE_URL: str = config("DATABASE_URL") # type: ignore

engine = create_engine(SQLALCHEMY_DATABASE_URL)

DBSession = sessionmaker(bind=engine, autoflush=False)

Base = declarative_base()