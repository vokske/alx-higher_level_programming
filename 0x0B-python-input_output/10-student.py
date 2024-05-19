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

    def to_json(self, attrs=None):
        """
        Retrieves a dictionary representation of a Student instance.

        Args:
            attrs (list): List of attribute names to retrieve.

        Returns (dict): Dictionary representation of the Student instance.
        """
        if attrs is None:
            return self.__dict__
        if isinstance(attrs, list) and all(isinstance(attr, str)\
                for attr in attrs):
            my_dict = {}

            for attr in attrs:
                if hasattr(self, attr):
                    my_dict[attr] = getattr(self, attr)
            return my_dict
        return self.__dict__
