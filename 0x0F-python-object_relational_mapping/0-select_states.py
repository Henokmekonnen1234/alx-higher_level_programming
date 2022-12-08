#!/usr/bin/python3

import MySQLdb
import sys

lists = sys.argv

if __name__ == "main":
    db = MySQLdb.connect("localhost", lists[1], lists[2], lists[3])
    
    cursor = db.cursor()

    cursor.execute("SELECT * FROM states")

    results = cursor.fetchall()
    for row in results:
        print(row)
