#!/usr/bin/python3
"""
list 10 commits (from the most recent to oldest)
"""

import sys
import requests

if __name__ == "__main__":
    repository_name, owner_name = sys.argv[1], sys.argv[2]
    url = "https://api.github.com/repos/{}/{}/commits".format(
            owner_name, repository_name)
    response = requests.get(url)
    commits = response.json()
    try:
        for i in range(10):
            print("{}: {}".format(
                commits[i].get("sha"),
                commits[i].get("commit").get("author").get("name")))
    except IndexError:
        pass
