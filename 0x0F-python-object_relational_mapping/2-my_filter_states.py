#!/usr/bin/python3

import MySQLdb
import sys
import re

lists = sys.argv
argument = re.split('; |, |\*|\n|\'|=', lists[4])

if __name__ == '__main__':
    db = MySQLdb.connect("localhost", lists[1], lists[2], lists[3])
    cursor = db.cursor()
    for args in argument:
        print(args)
        sql = "SELECT * FROM states WHERE name LIKE '%s'" % (args)
        cursor.execute(sql)
        results = cursor.fetchall()
        for rows in results:
            print("printed from rows, ", rows)
db.close()

