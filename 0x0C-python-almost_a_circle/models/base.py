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

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Write the JSON string representation of 'list_objs' to a file.

        Args:
            list_objs: List of instances that inherit from Base.
        """
        filename = cls.__name__ + ".json"

        if list_objs is None:
            list_dicts = []
        else:
            list_dicts = []
            for obj in list_objs:
                list_dicts.append(obj.to_dictionary())

        json_string = cls.to_json_string(list_dicts)

        with open(filename, "w") as f:
            f.write(json_string)

    @staticmethod
    def from_json_string(json_string):
        if json_string is None or len(json_string) == 0:
            return []
        else:
            return list(json.loads(json_string))

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
