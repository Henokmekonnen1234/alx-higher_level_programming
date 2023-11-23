#!/usr/bin/python3
"""
Module 4-cities_by_state.py

This module will list the city from DB
"""

if __name__ == "__main__":
    import MySQLdb
    import sys


    try:
        con = MySQLdb.connect(host="localhost", port=3306,
                              user=sys.argv[1], password=sys.argv[2],
                              db=sys.argv[3], charset="utf8")
        cur = con.cursor()
        cur.execute("SELECT cities.id, cities.name, states.name FROM cities\
                     INNER JOIN states WHERE states.id = cities.state_id\
                     ORDER BY cities.id")
        result = cur.fetchall()
        for value in result:
            print(value)
        cur.close()
        con.close()
    except (MySQLdb.Error, Exception) as e:
        cur.close()
        con.close()
        print(e)
