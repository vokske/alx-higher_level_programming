#!/usr/bin/python3
"""Module contains the class Base."""

import json


class Base:
    """
    Manages the id attribute.

    Private class attribute: __nb_objects.
    """

    __nb_objects = 0

    @staticmethod
    def to_json_string(list_dictionaries):
        """Return the JSON representation of 'list_dictionaries'."""

        if list_dictionaries is None or len(list_dictionaries) == 0:
            return f"{[]}"
        else:
            return json.dumps(list_dictionaries)

    def __init__(self, id=None):
        """
        Initialization of the Base class.

        Args:
            id: id of the instance. Initialized to "None".
        """

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
