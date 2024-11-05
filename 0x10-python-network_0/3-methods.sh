#!/bin/bash
# Script takes a URL and displays all the HTTP methods the server will accept
curl -sI "$1" | grep "Allow:" | cut -d ' ' -f2-
