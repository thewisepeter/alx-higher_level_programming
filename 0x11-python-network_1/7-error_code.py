#!/usr/bin/python3
"""
script that takes in a URLsends a request to the URL
displays the body of the response
"""

import sys
import requests

if __name__ == "__main__":
    url = sys.argv[1]
    response = requests.get(url)
    if response.status_code >= 400:
        print("Error code: {}".format(r.status_code))
    else:
        print(r.text)
