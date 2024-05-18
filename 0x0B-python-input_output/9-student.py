#!/usr/bin/python3
"""Module contains the class Student."""


class Student(object):
    """
    Defines a student.

    Methods:
        __init__
        to_json()

    Public atrributes:
        - first_name
        - last_name
        - age
    """
    def __init__(self, first_name, last_name, age):
        """
        Instantiation method.

        Args:
            first_name: Student's first name.
            last_name: Student's last name.
            age: Student's age.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Retrieves a dictionary representation of a Student instance."""
        return self.__dict__
