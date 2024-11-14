#!/usr/bin/python3
"""
Script sends a search request for a specific string to the Star Wars API. The request is sent to the Star Wars API search people endpoint.
"""

import sys, requests

if __name__ == "__main__":
    url = "https://swapi.dev/api/people"
    params = {'search': sys.argv[1]}
    r = requests.get(url, params=params).json()
    print(f"Number of results: {r['count']}")
    for item in r['results']:
        print(item['name'])
