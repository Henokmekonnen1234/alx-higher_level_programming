#!/usr/bin/python3
"""
Module 1-filter_states.py

This module will retrive data from hbtn_0e_0_usa database data
the names must start with letter N
"""

import MySQLdb
import sys

try:
    conn = MySQLdb.connect(host="localhost", port=3306,
                           user=sys.argv[1], password=sys.argv[2],
                           db=sys.argv[3], charset="utf8")
    cur = conn.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE \"N%\"\
                 ORDER BY states.id")
    result = cur.fetchall()
    for values in result:
        print(values)
except (MySQLdb.Error, Exception) as e:
    print(e)
cur.close()
conn.close()
