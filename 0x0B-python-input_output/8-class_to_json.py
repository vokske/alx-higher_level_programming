#!/usr/bin/python3
"""Module contains the class_to_json function."""


def class_to_json(obj):
    """
    Returns the dictionary description withsimple data structure.

    Args:
        obj: Specified Python object.
    """
    return vars(obj)
