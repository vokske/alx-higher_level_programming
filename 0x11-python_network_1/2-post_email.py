#!/usr/bin/python3
"""
Module takes a URL and an email as arguments, sends a POST request to the URL and displays the body of the response decoded in utf-8
"""

import sys, urllib.request, urllib.parse

if __name__ == "__main__":

    url = sys.argv[1]
    email = sys.argv[2]

    data = urllib.parse.urlencode({'email': email}).encode('utf-8')
    with urllib.request.urlopen(url, data) as f:
        print(f.read().decode('utf-8'))
