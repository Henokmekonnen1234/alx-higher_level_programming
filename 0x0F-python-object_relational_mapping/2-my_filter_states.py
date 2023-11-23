#!/usr/bin/python3
"""
Module 2-my_filter_states.py

This module will display fetched data given by the user
from hbtn_0e_0_usa
"""

if __name__ == "__main__":
    import MySQLdb
    import sys

    try:
        conn = MySQLdb.connect(host="localhost", port=3306,
                               user=sys.argv[1], password=sys.argv[2],
                               db=sys.argv[3], charset="utf8")
        cur = conn.cursor()
        cur.execute(f"SELECT * FROM states WHERE name = '{sys.argv[4]}'")
        result = cur.fetchall()
        for values in result:
            print(values)
        cur.close()
        conn.close()
    except (MySQLdb.Error, Exception) as e:
        cur.close()
        conn.close()
        pass
