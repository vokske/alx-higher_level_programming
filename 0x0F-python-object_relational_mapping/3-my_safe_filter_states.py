#!/usr/bin/python3

"""
Script displays all values in the states table from the database hbtn_0e_0_usa where the name matches the argument.

The script is safe from SQL injections.
"""

import sys
import MySQLdb

if __name__ == "__main__":
    
    db = MySQLdb.connect(host='localhost', port=3306, user=sys.argv[1], password                         =sys.argv[2], db=sys.argv[3])

    curs = db.cursor()

    query = "SELECT * FROM states WHERE name = %s;"

    curs.execute(query, (sys.argv[4],))

    states = curs.fetchall()

    for state in states:
        print(state)

    curs.close()
    db.close()
