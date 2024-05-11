#!/usr/bin/python
"""Module contains function lookup."""


def lookup(obj):
    """
    Returns the list of all available attributes and methods of an object.

    Args:
        obj: Object.
    """
    return dir(obj)
