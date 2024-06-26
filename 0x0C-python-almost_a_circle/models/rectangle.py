#!/usr/bin/python3
"""Contains a class Rectangle that inherits from Base."""


import json
from models.base import Base


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
        """
        Class constructor to initialize all instance attributes.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
            x (int): The x-coordinate in relation to the rectangle.
            y (int): The y-coordinate in relation to the rectangle.
            id (int): Id of the instance. Initialized to 'None'.

        Raises:
            TypeError: If width, height, x, or y is not an integer.
            ValueError: If width or height is <= 0. Also, if x or y < 0.
        """

        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """Retrieves width."""
        return self.__width

    @width.setter
    def width(self, value):
        """Validates the value of width."""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Retrieves height."""
        return self.__height

    @height.setter
    def height(self, value):
        """Validates the value of height."""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Retrieves the x-coordinate."""
        return self.__x

    @x.setter
    def x(self, value):
        """Validates the value of x."""
        if type(value) is not int:
            raise TypeError(f"x must be an integer")
        if value < 0:
            raise ValueError(f"x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Retrieves the y-coordinate."""
        return self.__y

    @y.setter
    def y(self, value):
        """Validates the value of y."""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Returns the area of the Rectangle instance."""
        return self.__width * self.__height

    def display(self):
        """Prints the Rectangle instance in stdout using '#'."""
        for _ in range(self.y):
            print()
        for row in range(self.height):
            print(" " * self.x + "#" * self.width)

    def __str__(self):
        """Return a custom representation of the Rectangle."""
        return f"[Rectangle] ({self.id}) {self.x}/{self.y} - \
{self.width}/{self.height}"

    def update(self, *args, **kwargs):
        """
        Assign a key/value argument to attributes.

        Args:
            *args: Variable length argument list in order.
        """

        if args and len(args) != 0:
            attrs = ["id", "width", "height", "x", "y"]
            for i, arg in enumerate(args):
                if i < len(attrs):
                    setattr(self, attrs[i], arg)
        else:
            for key, value in kwargs.items():
                if hasattr(self, key):
                    setattr(self, key, value)

    def to_dictionary(self):
        """Return a dictionary representation of a Rectangle instance."""
        return {
                "id": self.id,
                "width": self.width,
                "height": self.height,
                "x": self.x,
                "y": self.y
                }
