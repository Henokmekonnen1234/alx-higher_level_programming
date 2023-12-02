#!/usr/bin/python3
"""
Module 5-hbtn_header.py
this will takes in a URL, sends a request to the URL and displays the
value of the variable X-Request-Id in the response header"""

import requests
import sys

if __name__ == "__main__":
    try:
        response = requests.get("{}".format(sys.argv[1]))
        print(response.headers["X-Request-Id"])
    except Exception as e:
        print(e)
