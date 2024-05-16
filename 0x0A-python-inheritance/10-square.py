#!/usr/bin/python3
"""Module contains the Square class."""


Rectangle = __import__('9-Rectangle').Rectangle


class Square(Rectangle):
    """
    A class that inherits from Rectangle.

    Methods:
        __init__
        area()
    """

    def __init__(self, size):
        """
        Method to initialize size argument.

        Args:
            size(int): Size of square side.
        """
        self.__size = size
        self.integer_validator("size", size)

    def area(self):
        return self.__size ** 2
