#!/usr/bin/python3
"""
A module containing class Rectangle.
"""


class Rectangle:
    """Class with area and perimeter calculation methods.
    Attributes:
        number_of_instances(int): Number of objects created.
    """
    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """Initializes an instance of the class.
        Args:
            width (int, optional): Width of rectangle.
            height (int, optional): Height of rectangle.
        """
            self.__width = width
            self.__height = height
            type(self).number_of_instances += 1

    @property
    def width(self):
        """int: width of rectangle.
        Raises:
            TypeError: if not an integer.
            ValueError: if less than 0.
        Returns:
            Width of rectangle.
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
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """int: height of rectangle.
        Raises:
            TypeError: if not an integer.
            ValueError: if less than 0.
        Returns:
            Height of rectangle.
        """
        return (self.__height)

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Calculates and returns the area of rectangle.
        Returns:
            Area of rectangle.
        """
        return (self.__width * self.__height)

    def perimeter(self):
        """Calculates and returns the perimeter of rectangle.
        Returns:
            Perimeter of the rectangle.
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return (2 * (self.__width + self.__height))

    def __str__(self):
        """String representation of rectangle class.
        Returns:
            Character '#' representing the area.
        """
        if self.__width == 0 or self.__height == 0:
            return ("")
        rectangle_str = ["#" * self.__width for i in range(self.__height)]
        return ("\n".join(rectangle_str))

    def __repr__(self):
        """String representation of rectangle class.

        Returns:
            A square printed out with '#'.
        """
        return ("{}({}, {})".format(self.__class__.__name__, self.__width,
                self.__height))

    def __del__(self):
        """Deletes a class instance and prints a message.
        """
        type(self).number_of_instances -= 1
        print("Bye rectangle...")
