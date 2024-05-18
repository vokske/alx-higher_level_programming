#!/usr/bin/python3
"""Module contains the save_to_json_file function."""

import json


def save_to_json_file(my_obj, filename):
    """
    Writes an Object to a text file using a JSON representation.

    Args:
        my_obj: Specified Python object.
        filename: Name of the file to which the object is to be written.
    """
    with open(f"{filename}", "w") as fn:
        json.dump(my_obj, fn)
