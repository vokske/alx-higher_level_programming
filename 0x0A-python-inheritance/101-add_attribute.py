#!/usr/bin/python3
"""Module contains function add_attribute."""


def add_attribute(obj, attr, value):
    """
    Add a new attribute to an object if it's possible.

    Args:
        obj: Object to which the attribute will be added.
        attr: Name of the attribute to be added.
        value: Value of the attribute.

    Raises:
        TypeError: If the object cannot have a new attribute.
    """
    if hasattr(obj, '__dict__'):
        setattr(obj, attr, value)
    else:
        raise TypeError("can't add new attribute")
