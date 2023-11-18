#!/usr/bin/python3
"""
  Module 0-select_states.py
This module will be explained below
"""

import MySQLdb
import sys

try:
    conn = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                        password=sys.argv[2], db=sys.argv[3], charset="utf8")
    cur = conn.cursor()
    cur.execute("SELECT * FROM states ORDER BY states.id")
    row = cur.fetchall()
    for items in row:
        print(items)
except (MySQLdb.Error, Exception) as e:
    print("{}".format(e))
cur.close()
conn.close()
