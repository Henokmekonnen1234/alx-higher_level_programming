#!/usr/bin/python3
"""
Module 6-post_email.py
This module will takes in a URL and an email address, sends a POST
request to the passed URL with the email as a parameter, and finally
displays the body of the response."""

import requests
import sys

if __name__ == "__main__":
    try:
        data = {"email": "{}".format(sys.argv[2])}
        response = requests.post("{}".format(sys.argv[1]), data=data)
        print("{}".format(response.text))
    except Exception as e:
        print("{}".format(e))
