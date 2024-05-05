#!/usr/bin/python3
"""Module contains the print_square function."""


def print_square(size):
    """
    Prints a square with the character #.

    Args:
        size(int): Length of the square.

    Raises:
        TypeError: if size isn't an integer or is a float and is less than 0
        ValueError: if size is less than 0

    Returns: nothing.
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        for j in range(size):
            print("{}".format("#"), end="")
        print()
