#!/usr/bin/python3

"""File contains the class definition of a State and an instance of Base class."""

from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import Column, Integer, String

Base = declarative_base()

class State(Base):

   """
   Attributes:

   __tablename__ (str): Name of the MySQL table.
   
   id (int): Unique identification number for a state.
   
   name (str): Name of a state.
   """

    __tablename__ = "states"

    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
