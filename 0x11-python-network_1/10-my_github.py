#!/usr/bin/python3
"""
script that takes your GitHub credentials
and displays my id
"""

import sys
import requests
from requests.auth import HTTPBasicAuth
if __name__ == "__main__":
    username, password = sys.argv[1], sys.argv[2]
    auth_user = HTTPBasicAuth(username, password)
    response = requests.get("https://api.github.com/user", auth=auth_user)
    print(response.json().get("id"))
