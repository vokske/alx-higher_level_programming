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

    def area(self):
        """
        Computes and returns the area of the rectangle.
        """
        return self.__width * self.__height

    def __str__(self):
        return(f"[Rectangle] {self.__width}/{self.__height}")

