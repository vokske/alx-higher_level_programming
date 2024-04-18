#!/usr/bin/python3

"""
    Defines square by size.
"""


class Square:
    """
    Represents a square.

    Attributes:
        size(int): The length of each side of the sqaure.

    Methods:
        None

    Usage:
        Create an instance of the Square class.
    """

    def __init__(self, size):
        """
        Initializes a Square instance with the provided size.

        Args:
            size(int): The length of the side of the square
        """
        self.__size = size
