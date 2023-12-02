#!/usr/bin/python3
"""
Module 7-error_code.py
This module will takes in a URL, sends a request to the
URL and displays the body of the response."""

import requests
import sys

if __name__ == "__main__":
    try:
        response = requests.get("{}".format(sys.argv[1]))
        if response.status_code >= 400:
            print("Error code: {}".format(response.status_code))
        else:
            print("{}".format(response.text))
    except Exception as e:
        print("{}".format(e))
