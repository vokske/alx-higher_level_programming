#!/usr/bin/python3

"""
Script lists all cities from the database hbtn_0e_0_usa
"""
import sys
import MySQLdb

if __name__ == "__main__":
    
    db = MySQLdb.connect(host='localhost', port=3306, user=sys.argv[1], password                         =sys.argv[2], db=sys.argv[3])

    curs = db.cursor()

    query = "SELECT cities.id, cities.name, states.name FROM cities JOIN states ON cities.state_id = states.id;"

    curs.execute(query)

    states = curs.fetchall()

    for state in states:
        print(state)

    curs.close()
    db.close()
