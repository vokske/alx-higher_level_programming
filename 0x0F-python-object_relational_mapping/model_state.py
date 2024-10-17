#!/usr/bin/python3

import sys
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class State(Base):
    __table__name = "states"

    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
