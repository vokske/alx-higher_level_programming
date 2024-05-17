#!/usr/bin/python3
"""Module contains the to_json_string function."""
import json


def to_json_string(my_obj):
    """
    Gives the JSON representation of an object.

    Args:
        my_obj: Specified object.
    """
    return json.dumps(my_obj)
