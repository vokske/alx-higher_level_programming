#!/usr/bin/python3
"""Module contains the class Square."""

from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Represents a square.

    Methods:
        __init__
    """

    def __init__(self, size, x=0, y=0, id=None):
        """Initializes the square."""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Retrieve the size of the square."""
        return self.width

    @size.setter
    def size(self, value):
        """Set the value of size."""
        self.width = value
        self.height = value

    def __str__(self):
        """Return the string representation of the square."""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"
