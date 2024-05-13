#!/usr/bin/python3
"""Module contains class BaseGeometry."""


class BaseGeometry:
    """
    Class named BaseGeometry.

    Methods:
        area
        integer_validator
    """
    def area(self):
        """
        Area method.

        Raises:
            Exception with custom message.
        """
        raise Exception("area() is not implemented")
    
    def integer_validator(self, name, value):
        """
        validates value.

        Args:
            name: Name of object.
            value: Value of object.

        Raises:
            TypeError: if value is not an integer.
            ValueError: if value is less or equal to 0.
        """
        if type(value) is not int:
            raise TypeError("<name> must be an integer")
        if value <= 0:
            raise ValueError("<name> must be greater than 0")
