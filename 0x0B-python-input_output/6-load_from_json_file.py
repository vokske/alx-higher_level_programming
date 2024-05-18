#!/usr/bin/python3
"""Module contains the load_from_json_file function."""

import json


def load_from_json_file(filename):
    """
    Creates a Python object from a file containing JSON data.

    Args:
        filename: Name of the JSON file.
    """
    with open(f"{filename}", "r") as readFile:
        json.load(readFile)
