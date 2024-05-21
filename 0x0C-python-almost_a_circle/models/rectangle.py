#!/usr/bin/python3
"""Contains a class Rectangle that inherits from Base."""

from base import Base

class Rectangle(Base):
    """
    Represents a rectangle.

    Private attributes:
        - __width
        - __height
        - __x
        - __y

    Methods
        __init__
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)

    @property
    def width(self):
        return self.__width

    @property
    def height(self):
        return self.__height

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError(f"{self.__width} must be an integer")
        if value <= 0:
            raise ValueError(f"{self.__width} must be >= 0")
        self.__width = value

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError(f"{self.__height} must be an integer")
        if value <= 0:
            raise ValueError(f"{self.__height} must be >= 0")
        self.__height = value

    @x.setter
    def x(self, value):
        if type(value) is not int:
            raise TypeError(f"{self.__x} must be an integer")
        if value <= 0:
            raise ValueError(f"{self.__x} must be >= 0")
        self.__x = value

    @y.setter
    def y(self, value):
        if type(value) is not int:
            raise TypeError(f"{self.__y} must be an integer")
        if value <= 0:
            raise ValueError(f"{self.__y} must be >= 0")
        self.__y = value
