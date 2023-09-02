#!/usr/bin/python3
"""
script that takes in a URLsends a request to the URL
displays the value of the X-Request-Id variable
"""

import sys
import urllib.request

if __name__ == "__main__":
    url = sys.argv[1]
    request = urllib.request.Request(url)
    with urllib.request.urlopen(request) as response:
        headers = dict(response.headers)
        print(headers.get("X-Request-Id"))
