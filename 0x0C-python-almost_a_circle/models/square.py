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

    def update(self, *args, **kwargs):
        """Update a Square instance with args or kwargs."""

        attrs = ["id", "size", "x", "y"]

        if args and len(args) != 0:
            for i, arg in enumerate(args):
                if i < len(attrs):
                    setattr(self, attrs[i], arg)
        else:
            for key, value in kwargs.items():
                if hasattr(self, key):
                    setattr(self, key, value)
