#!/usr/bin/python3
"""Module contains class Rectangle."""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):

    """
    Class that inherits from BaseGeometry.

    Methods:
        __init__
    """

    def __init__(self, width, height):
        """
        Initializes width and height.

        Args:
            width(int): width of rectangle.
            height(int): height of rectangle.
        """
        self.__width = width
        self.__height = height
        self.integer_validator("width", width)
        self.integer_validator("height", height)
