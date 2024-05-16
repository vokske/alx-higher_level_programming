#!/usr/bin/python3
"""Module contains the Square class."""


Rectangle = __import__('9-rectangle').Rectangle


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
        """
        Computes and returns the area of a square.
        """
        return self.__size ** 2

    def __str__(self):
        """
        Magic string method.

        Returns: Custom square description.
        """
        return f"[{__class__.__name__}] {self.__width}/{self.__height}"
