#!/usr/bin/python3

"""0_add_integer contains a function that add 2 integers."""


def add_integer(a, b=98):
    """
    Adds two integers.

    Args:
        a (int, float): The first number
        b (int, float): The second number. Defaults to 98.

    Returns:
        int: The sum of a and b

    Raises:
        TypeError: If a or b isn't an int or float.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    if type(a) is float or type(b) is float:
        a = int(a)
        b = int(b)
    return a + b
