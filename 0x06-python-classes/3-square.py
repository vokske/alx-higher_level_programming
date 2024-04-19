#!/usr/bin/python3
"""Defines a class Square."""


class Square:
    """Represents a square."""
    

    def __init__(self, size):
        """
        Initializes a Square instance.


        Args:
            Size(int): The size of the side of the square.
        """

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self._Square__size = size

    def area(self):
        """Returns the area of a square."""
        return self._Square__size ** 2
