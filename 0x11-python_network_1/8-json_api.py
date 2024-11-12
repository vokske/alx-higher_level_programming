#!/usr/bin/python3
"""
Script takes in a letter and sends a POST request to http://0.0.0.0:5000/search_user with the letter as a parameter (sent in the variable q). For a non-empty and JSON formatted response body, display the id and name in the form [<id>] <name>. Otherwise, display 'Not a valid JSON' if the JSON is invalid or 'No result' if JSON is empty.
"""

import sys, requests

if __name__ == "__main__":

    if len(sys.argv) == 2:
        q = sys.argv[1]
    else:
        q = ""

    payload = {'letter': q}
    r = requests.post('http://0.0.0.0:5000/search_user', data=payload)
    try:
        response = r.json()
        if response == {}:
            print("No Result")
        else:
            print(f"[{response.get('id')}] {response.get('name')}")
    except ValueError:
        print("Not a valid JSON")
