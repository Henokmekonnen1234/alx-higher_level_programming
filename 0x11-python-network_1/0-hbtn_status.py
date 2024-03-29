#!/usr/bin/python3
"""
module 0-hbtn_status.py
this python code will fetch from the given link
"""

import urllib.request

if __name__ == "__main__":
    try:
        with urllib.request.urlopen("https://alx-intranet.hbtn.io/status"
                                    ) as body_response:
            result_response = body_response.read()
        print("Body response:")
        print("\t- type: {}".format(type(result_response)))
        print("\t- content: {}".format(result_response))
        print("\t- utf8 content: {}".format(result_response.decode("utf-8")))
    except Exception as e:
        print(e)
