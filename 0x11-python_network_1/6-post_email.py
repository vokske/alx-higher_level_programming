#!/usr/bin/python3
"""
Script takes in a URL and email as CL arguments, sends a POST request to the URL with email as parameter and displays the body of the response.
"""

import sys, requests

if __name__ == "__main__":

    r = requests.post(sys.argv[1], data={'email': sys.argv[2]})
    print(r.text)
