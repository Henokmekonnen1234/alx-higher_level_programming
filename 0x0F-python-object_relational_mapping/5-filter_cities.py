#!/usr/bin/python3
"""
Module 5-filter_cities.py

This module will list the cities in a given state
"""

if __name__ == "__main__":
    import MySQLdb
    import sys

    try:
        con = MySQLdb.connect(host="localhost", port=3306,
                              user=sys.argv[1], password=sys.argv[2],
                              db=sys.argv[3], charset="utf8")
        cur = con.cursor()
        cur.execute("SELECT cities.name FROM cities INNER JOIN states\
                     WHERE states.name = %s AND\
                     states.id = cities.state_id ORDER BY cities.id",
                     (sys.argv[4],))
        result = cur.fetchall()
        result = list(map(lambda x: x[0], result))
        for i in range(len(result)):
            print(result[i], end="")
            if i != len(result) - 1:
                print(", ", end="")
        print()
        cur.close()
        con.close()
    except (MySQLdb.Error, Exception) as e:
        cur.close()
        con.close()
        print(e)
