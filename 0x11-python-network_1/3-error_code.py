#!/usr/bin/python3
"""
script that takes in a URLsends a request to the URL
displays the body of the response
"""

import sys
import urllib.request
import urllib.request

if __name__ == "__main__":
    url = sys.argv[1]
    request = urllib.request.Request(url)
    try:
        with urllib.request.urlopen(request) as response:
            content = response.read().decode('ascii'))
            print(content)
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))
