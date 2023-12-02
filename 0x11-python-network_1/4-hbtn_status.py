#!/usr/bin/python3
"""
Module 4-hbtn_status.py
This will  fetches https://alx-intranet.hbtn.io/status
"""

import requests

if __name__ == "__main__":
    try:
        response = requests.get("https://alx-intranet.hbtn.io/status")
        print("Body response:")
        print("\t-type: {}".format(type(response.text)))
        print("\t-content: {}".format(response.content.decode("utf-8")))
    except Exception as e:
        print(e)
