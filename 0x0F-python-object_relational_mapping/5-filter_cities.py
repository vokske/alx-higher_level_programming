#!/usr/bin/python3

"""
Script lists all the cities of the state supplied as an argument using the database hbtn_0e_4_usa
"""
import sys
import MySQLdb

if __name__ == "__main__":
    
    db = MySQLdb.connect(host='localhost', port=3306, user=sys.argv[1], password                         =sys.argv[2], db=sys.argv[3])

    curs = db.cursor()

    query = "SELECT cities.name FROM cities JOIN states ON cities.state_id = states.id WHERE states.name = %s;"

    curs.execute(query, (sys.argv[4],))

    cities = curs.fetchall()

    printed_cities = ', '.join(city[0] for city in cities)

    print(printed_cities)

    curs.close()
    db.close()
