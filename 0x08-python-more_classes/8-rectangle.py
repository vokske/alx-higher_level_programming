#!/usr/bin/python3
"""
A module containing class Rectangle."""


class Rectangle:
    """Represents a rectangle.

    Attributes:
        number_of_instances(int): Total number of objects created.
        print_symbol (any): Symbol for string representation.

    Methods:

        __init__(self, width=0, height=0):
            Initializes an instance of the class Rectangle.

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
    print_symbol = '#'

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Returns the biggest rectangle based on the area.

        Args:
            rect_1 (Rectangle): First rectangle.
            rect_2 (Rectangle): Second rectangle.
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        area_1 = rect_1.area()
        area_2 = rect_2.area()

        if area_1 >= area_2:
            return rect_1
        return rect_2

    def __init__(self, width=0, height=0):
        """Initializes width and height.
        Args:
            width (int, optional): Width of rectangle.
            height (int, optional): Height of rectangle.
        """
        self.__width = width
        self.__height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Returns the width of the rectangle.

        Raises:
            TypeError: if width is not an integer.
            ValueError: if width is less than 0.

        Returns:
            Width of rectangle.
        """
        return (self.__width)

    @width.setter
    def width(self, value):
        """Sets the value of width.

        Raises:
            TypeError: if value is not an integer.
            ValueError: if value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """Return the  height of the rectangle.

        Raises:
            TypeError: if height is not an integer.
            ValueError: if height is less than 0.
        Returns:
            Height of the rectangle.
        """
        return (self.__height)

    @height.setter
    def height(self, value):
        """Sets the value of height.

        Raises:
            TypeError: if value is not an integer.
            ValueError: if value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """Calculates area of rectangle.
        Returns:
            Area of rectangle.
        """
        return (self.__width * self.__height)

    def perimeter(self):
        """Calculates perimeter of rectangle.
        Returns:
            Perimeter of rectangle.
        """
        if self.__width == 0 or self.__height == 0:
            return (0)
        else:
            return (2 * (self.__width + self.__height))

    def __str__(self):
        """String representation of rectangle class.
        Returns:
            Character '#' representing the area.
        """
        if self.__width == 0 or self.__height == 0:
            return ""
        return ("\n".join([str(self.print_symbol) * self.__width]
                * self.__height))

    def __repr__(self):
        """String repr of rectangle class.
        Returns:
            Formatted string representation.
        """
        return ("{}({}, {})".format(self.__class__.__name__, self.__width,
                self.__height))

    def __del__(self):
        """Deletes a class instance and prints a message.
        """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
