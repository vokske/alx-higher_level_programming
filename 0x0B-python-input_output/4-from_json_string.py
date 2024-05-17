#!/usr/bin/python3
"""Module contains the function from_json_string."""

import json


def from_json_string(my_str):
    """
    Returns a Python object represented by a JSON string.

    Args:
        my_str: Specified JSON string.
    """
    return json.loads(my_str)
