#!/usr/bin/python3
"""
Module fetches https://alx-intranet.hbtn.io/status using the requests package.
"""

import requests

if __name__ == "__main__":
    url = 'https://alx-intranet.hbtn.io/status'
    r = requests.get(url)
    print("Body Response:")
    print(f"\t- type: {type(r.text)}")
    print(f"\t- content: {r.text}")
