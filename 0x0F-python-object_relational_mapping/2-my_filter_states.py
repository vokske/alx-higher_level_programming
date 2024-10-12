#!/usr/bin/python3

"""
Script lists all values in a table from the database hbtn_0e_0_usa whose name matches the argument
"""
import sys
import MySQLdb

if __name__ == "__main__":
    
    db = MySQLdb.connect(host='localhost', port=3306, user=sys.argv[1], password                         =sys.argv[2], db=sys.argv[3])

    curs = db.cursor()

    query = "SELECT * FROM states WHERE name = '{}';".format(sys.argv[4])

    curs.execute(query)

    states = curs.fetchall()

    for state in states:
        print(state)

    curs.close()
    db.close()
