#!/usr/bin/python3

import sys
from model_state import Base, State
from model_city import City
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

if __name__ == "__main__":

    db_url = f'mysql+mysqldb://{sys.argv[1]}:{sys.argv[2]}@localhost:3306/{sys.argv[3]}'

    engine = create_engine(db_url)

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)

    session = Session()

    cities = session.query(State, City).join(City, State.id == City.state_id)

    for state, city in cities:
        print(f"{state.name}: ({city.id}) {city.name}")
