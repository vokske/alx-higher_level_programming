#!/usr/bin/python3
"""
Script takes a URL, sends a request to it and displays the body of the response. The message 'Error code: {HTTP status code}' is shown if the HTTP status code value is greater than or equal to 400.
"""

import sys, requests

if __name__ = "__main__":
    url = sys.argv[1]
    r = requests.get(url)

    if r.status_code >= 400:
        print(f"Error code: {r.status_code}")
    print(r.text)
