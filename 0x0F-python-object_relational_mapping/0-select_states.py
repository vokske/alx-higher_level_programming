#!/usr/bin/python3

"""
Script lists all states from the database hbtn_0e_0_usa
"""
import sys
import MySQLdb

if __name__ == "__main__":
    
    db = MySQLdb.connect(host='localhost', port=3306, user=sys.argv[1], password                         =sys.argv[2], db=sys.argv[3])

    curs = db.cursor()

    curs.execute("SELECT * FROM states ORDER BY id ASC")

    states = curs.fetchall()

    for state in states:
        print(state)

    curs.close()
    db.close()
