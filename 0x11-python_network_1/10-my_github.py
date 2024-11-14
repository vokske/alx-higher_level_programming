#!/usr/bin/python3
"""
Script takes GitHub credentials and uses the GitHub API to display the id. Use Basic authentication with personal access token (PAT) as the password.
The first CL argument is the username, the second is the password.
"""

import sys, requests
from requests.auth import HTTPBasicAuth

if __name__ == "__main__":
    auth = HTTPBasicAuth(sys.argv[1], sys.argv[2])
    response = requests.get("https://api.github.com/user", auth=auth)
    print(response.json().get('id'))
