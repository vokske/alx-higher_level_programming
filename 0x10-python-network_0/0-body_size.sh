#!/bin/bash
# Script takes a URL, sends a request to the URL, and displays the size of the response's body.
curl -s "$1" | wc -c
