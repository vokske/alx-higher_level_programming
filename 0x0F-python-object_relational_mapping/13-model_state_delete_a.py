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

    states = session.query(State).filter(State.name.like('%t%'))

    [session.delete(state) for state in session.query(State).filter(State.name.like('w%'))]

    session.commit()

# Alternative method:
# Import delete method from sqlalchemy
# session.execute(delete(State).where(State.name.like('%a%')))
# session.commit()
