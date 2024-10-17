#!/usr/bin/python3

import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":

    engine = create_engine(f'mysql+mysqldb://{sys.argv[1]}:{sys.argv[2]}@localhost:3306/{sys.argv[3]}')

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)

    session = Session()

    get_state = sys.argv[4]

    state = session.query(State).filter(State.name == get_state).all()

    if not state:
        print("Not found")

    else:
        for element in state:
            print(element.id)
