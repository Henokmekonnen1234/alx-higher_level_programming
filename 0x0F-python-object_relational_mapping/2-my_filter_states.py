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
        conn = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1]
