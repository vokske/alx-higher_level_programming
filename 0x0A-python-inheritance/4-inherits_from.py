#!/usr/bin/python3
"""Module contains function inherits_from."""


def inherits_from(obj, a_class):
    """
    Checks if object is an instance of a class that inherited from the
    specified class.

    Args:
        obj: Object.
        a_class: Specified class.

    Returns:True if object is an instance of a class that inherited from
            specified class. False otherwise.
    """
    return issubclass(type(obj), a_class) and type(obj) is not a_class
