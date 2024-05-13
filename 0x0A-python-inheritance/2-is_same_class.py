#!/usr/bin/python3
"""Module contains function is_same_class."""


def is_same_class(obj, a_class):
    """
    Checks if an object is exactly an instance of a specified class.

    Args:
        obj: Object of a class.
        a_class: Specified class.

    Returns:
        True: if object is exactly an instance of the class. False otherwise.
    """
    return type(obj) is a_class
