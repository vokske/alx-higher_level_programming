#!/usr/bin/python3

"""
Module contains a script that fetches the url 'https://alx-intranet.hbtn.io/status'
"""
import urllib.request

if __name__ == "__main__":
    # We start by creating a Request object, which reps the HTTP Request we're
    # making or the URL we're fetching
    r = urllib.request.Request("https://alx-intranet.hbtn.io/status")

    with urllib.request.urlopen(r) as response:
        response = response.read()
        print("Body response:")
        print(f"\t- type: {type(response)}")
        print(f"\t- content: {response}")
        print(f"\t- utf8 content: {response.decode('utf-8')}")
