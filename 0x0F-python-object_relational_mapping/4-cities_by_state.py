#!/usr/bin/python3
"""
Module 4-cities_by_state.py

This module will list the city from DB
"""

if __name__ == "__main__":
    import MySQLdb
    import sys


    try:
        con = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
