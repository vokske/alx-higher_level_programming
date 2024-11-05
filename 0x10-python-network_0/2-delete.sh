#!/bin/bash
# Script sends a DELETE request to the URL passed and displays the body of the response.
curl -X DELETE -s "$1"
