#!/usr/bin/python3
"""
script that takes in a URLsends a request to the URL
displays the value of the X-Request-Id variable
"""

import sys
import urllib.request

url = sys.argv[1]
request = urllib.request.Request(url)
with urllib.request.urlopen(request) as response:
    headers = response.info()
    x_request_id = headers.get("X-Request-Id")
    if x_request_id:
        print(x_request_id)
    else:
        print("not found")


