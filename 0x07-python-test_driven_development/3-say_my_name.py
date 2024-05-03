#!/usr/bin/python3
"""Contains a function that says one's name."""
def say_my_name(first_name, last_name=""):
    """
    Prints one's name.

    Args:
        first_name (str): First name.
        last_name (str): Last name.

    Returns: Nothing

    Raises:
        TypeError: if first_name or last_name are not strings.
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print(f"My name is {first_name} {last_name}")
