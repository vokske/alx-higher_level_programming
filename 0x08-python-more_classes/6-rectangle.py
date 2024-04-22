#!/usr/bin/python3
"""
Module contains class rectangle.
"""


class Rectangle:
    """
    Represents a rectangle.

    Attributes:
        width (int): Width of the rectangle.
        height (int): Height of the rectangle.
        number_of_instances (int): Total number of instances created.

    Methods:

        __init__(self, width=0, height=0):
            Initializes an instance of the class Rectangle.

            Args:
                width (int, optional): The width of the rectangle.
                height (int, optional): The height of the rectangle.

        __str__(self):
            Returns a string representation of the rectangle using '#'.

            Returns:
                str: The string representation of the rectangle.

        __repr__(self):
            Returns a string representation of the rectangle for eval().

            Returns:
                str: String representation of the rectangle.

        __del__(self):
            Prints a message when an instance of class Rectangle is deleted.

        area(self):
            Calculates and returns the area of the rectangle.

            Returns:
                int: The area of the rectangle.

        perimeter(self):
            Calculates and returns the perimeter of the rectangle.

            Returns:
                int: The perimeter of the rectangle.
    """

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """Initializes an instance of the class Rectangle.

        Args:
            width (int, optional): The width of the rectangle.
            height (int, optional): The height of the rectangle.
        """
        self.width = width
        self.height = height
    Rectangle.number_of_instances += 1

    @property
    def width(self):
        """
        Retrieves the width of the rectangle.

        Returns:
            int: Width of the rectangle
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Sets the width.

        Args:
            value (int): The width value.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        Retrieves the height of the rectangle.

        Returns:
            int: The height of the rectangle.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Sets the height.

        Args:
            value (int): The width value.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        Calculates and returns the area of the rectangle.

        Returns:
            int: The area of the rectangle.
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        Calculates and returns the perimeter of the rectangle.

        Returns:
            int: The perimeter of the rectangle.
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """
        Returns a string representation of the rectangle using '#'.

        Returns:
            str: The string representation of the rectangle.
        """
        if self.__width == 0 or self.__height == 0:
            return ""
        return "\n".join(['#' * self.__width] * self.__height)

    def __repr__(self):
        """
        Returns a string representation of the rectangle for eval().

        Returns:
            str: String representation of the rectangle.
        """
        return("{}({}, {})".format(self.__class__.__name__, self.__width,
               self.__height))

    def __del__(self):
        """Prints a message when an instance of class Rectangle is deleted."""
        print("Bye rectangle...")
    Rectangle.number_of_instances -= 1
