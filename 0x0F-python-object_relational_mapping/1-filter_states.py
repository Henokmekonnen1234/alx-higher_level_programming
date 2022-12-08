#!/usr/bin/python3

import MySQLdb
import sys

lists = sys.argv
sql = "SELECT * FROM states WHERE name like 'N%'"
if __name__ == '__main__':
    db = MySQLdb.connect("localhost", lists[1], lists[2], lists[3])
    cursor = db.cursor()
    cursor.execute(sql)
    results = cursor.fetchall()
    for rows in results:
        print(rows)
