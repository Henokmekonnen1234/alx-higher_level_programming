#!/usr/bin/python3
"""
Module 2-post_email.py
This module will takes in a URL and an email, sends a POST request to the
passed URL with the email as a parameter,
and displays the body of the response """

import urllib.request
import urllib.parse
import sys

if __name__ == "__main__":
    try:
        if sys.argv[1] is not None and sys.argv[2] is not None:
            data = {"email":  f"{sys.argv[2]}"}
            data = urllib.parse.urlencode(data).encode("utf-8")
            request = urllib.request.Request(sys.argv[1], data,
                                             method="POST")
            with urllib.request.urlopen(sys.argv[1]) as response:
                body_content = response.encode("utf-8")
        print(body_content)
    except Exception as e:
        print(e)
