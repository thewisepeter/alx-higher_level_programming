#!/usr/bin/python3
"""
script that takes in a URLsends a request to the URL
displays the value of the X-Request-Id variable
"""

import sys
import requests

if __name__ == "__main__":
    url = sys.argv[1]
    payload = {'email': sys.argv[2]}
    
    response = requests.get(url, params=payload)
    print(response.url)
