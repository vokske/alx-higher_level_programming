#!/usr/bin/python3
"""
Module takes a URL, sends a request to it and displays the body of the response (decoded in utf-8). Also, manage urllib.error.HTTPError exceptions and print: Error code: followed by the HTTP status code.
"""

import sys, urllib.request, urllib.error

if __name__ == "__main__":
    url = sys.argv[1]

    request = urllib.request.Request(url)

    try:
        with urllib.request.urlopen(request) as r:
            r = r.read().decode('utf-8')
            print(response)

    except urllib.error.HTTPError as e:
        print(f"Error code: {e.code}")

