#!/usr/bin/python3
"""
Module contains a script that takes a URL as an argument, send a request to it, and displays the value of the X-Request-Id variable in the header of the response.
"""
import sys, urllib.request

if __name__ == "__main__":
    url = sys.argv[1]

    request = urllib.request.Request(url)

    with urllib.request.urlopen(request) as response:
        result = dict(response.headers).get('X-Request-Id')
        print(result)
