#!/usr/bin/python3
"""Contains a class Rectangle that inherits from Base."""


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

        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)

    @property
    def width(self):
        """Retrieves width."""
        return self.__width

    @property
    def height(self):
        """Retrieves height."""
        return self.__height

    @property
    def x(self):
        """Retrieves the x-coordinate."""
        return self.__x

    @property
    def y(self):
        """Retrieves the y-coordinate."""
        return self.__y

    @width.setter
    def width(self, value):
        """Validates the value of width."""
        if type(value) is not int:
            raise TypeError(f"{self.width.__name__} must be an integer")
        if value <= 0:
            raise ValueError(f"{self.width.__name__} must be > 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """Validates the value of height."""
        if type(value) is not int:
            raise TypeError(f"{self.__height} must be an integer")
        if value <= 0:
            raise ValueError(f"{self.height.__name__} must be > 0")
        self.__height = value

    @x.setter
    def x(self, value):
        """Validates the value of x."""
        if type(value) is not int:
            raise TypeError(f"{self.x.__name__} must be an integer")
        if value < 0:
            raise ValueError(f"{self.x.__name__} must be >= 0")
        self.__x = value

    @y.setter
    def y(self, value):
        """Validates the value of y."""
        if type(value) is not int:
            raise TypeError(f"{self.y.__name__} must be an integer")
        if value < 0:
            raise ValueError(f"{self.y.__name__} must be >= 0")
        self.__y = value
