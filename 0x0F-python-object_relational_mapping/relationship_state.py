#!/usr/bin/python3

from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy import Column, Integer, String

Base = declarative_base()

class State(Base):
    __tablename__ = "states"

    id = Column(Integer, primary_key=True, nullable=False)

    name = Column(String(128), nullable=False)

    cities = relationship("City", back_populates="states")
