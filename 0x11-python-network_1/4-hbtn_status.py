#!/usr/bin/python3
"""
Python script that fetches https://alx-intranet.hbtn.io/status
"""
import requests
if __name__ == "__main__":
    response = requests.get('https://alx-intranet.hbtn.io/status')
    content = response.read()
    content_utf8 = content.decode('utf-8')
    print("Body response:")
    print("\t- type:", type(content))
    print("\t- content:", content)
    print("\t- utf8 content:", content_utf8)
