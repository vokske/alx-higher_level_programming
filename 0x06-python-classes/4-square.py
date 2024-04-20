#!/usr/bin/python3
"""Defines a class Square."""


class Square:
    """Represents a square."""
    def __init__(self, size=0):
        """
        Initializes a Square instance.


        Args:
            Size(int): The size of the side of the square.
        """
        self.size = size

    @property
    def size(self):
        """Retrieves the size"""
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the value for size"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Returns the area of a square."""
        return value ** 2
