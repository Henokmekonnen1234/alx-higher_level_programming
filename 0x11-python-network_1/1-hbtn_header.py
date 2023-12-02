#!/usr/bin/python3
"""
Module 1-hbtn_header.py
This module will take url and sends a request to the URL and displays
the value of the X-Request-Id
"""

from urllib.request import urlopen
import sys

if __name__ == "__main__":
    try:
        if sys.argv[1] is not None:
            with urlopen(sys.argv[1]) as response:
                x_request_id = response.getheader("X-Request-Id")
        print(x_request_id)
    except Exception as e:
        print(e)
