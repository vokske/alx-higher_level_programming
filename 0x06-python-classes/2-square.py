#!/usr/bin/python3

"""
Module that defines a square.

Classes:
    (None)
Exceptions:
    (None)
Functions:
    (None)
"""


class Square:
    """
    Defines a square.
    
    Attributes:
        Size(int): The length of each side of the square.

    Methods:
        __init__(self, size=0): Initializes a square instance.

    Usage:
        Create an instance of the Square class.
    """

    def __init__(self, size=0)
        """
        Initializes a Square instance with the provided size.

        Args:
            size(int): The lenght of the side of the square
        Raises:
            TypeError: if size is not an integer
            ValueError: if size is less than 0
        """

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if value.isdigit():
            self.__size = value
        else:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("Size must be >= 0")
        self.__size = size