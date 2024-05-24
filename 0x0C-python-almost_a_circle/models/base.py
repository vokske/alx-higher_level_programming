#!/usr/bin/python3
"""Module contains the class Base."""

import json
import csv


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
        """
        Convert json_string to a list of dictionaries.

        Args:
            json_string: A string representing a list of dictionaries

        Returns: The list of the JSON string representation json_string.
        """

        if json_string is None or len(json_string) == 0:
            return []
        else:
            return list(json.loads(json_string))

    @classmethod
    def create(cls, **dictionary):
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """Reads json file and returns a list of instances,"""

        filename = f"{cls.__name__}.json"

        try:
            with open(filename, 'r') as fn:
                json_string = fn.read()
            list_dicts = cls.from_json_string(json_string)
            instances = []
            for item in list_dicts:
                instance = cls.create(**item)
                instances.append(instance)
            return instances
        except FileNotFoundError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """
        Do a CSV serialization.

        Args:
            list_objs: List of instances that inherit from Base.
        """

        filename = f"{cls.__name__}.csv"
        with open(filename, 'r', newline='') as f:
            writer = csv.writer(f)
            if cls.__name__ == "Rectangle":
                for obj in list_objs:
                    writer.writerow([obj.id, obj.width, obj.height, 
                                    obj.x, obj.y])
            elif cls.__name__ == "Square":
                for obj in list_objs:
                    writer.writerow([obj.id, obj.size, obj.x, obj.y])

    @classmethod
    def load_from_file_csv(cls):
        """Does CSV deserialization."""

        filename = f"{cls.__name__}.csv"
        try:
            with open(filename, 'r', newline='') as f:
                reader = csv.reader(f)
                instances = []
                for row in reader:
                    if cls.__name__ == "Rectangle":
                        id, width, height, x, y = map(int, row)
                        instance = cls.create(id=id, width=width, height=height,                                              x=x, y=y)
                    elif cls.__name__ == "Square":
                        id, size, x, y = map(int, row)
                        instance = cls.create(id=id, size=size, x=x, y=y)
                    instance.append(instance)
                return instances
            except FileNotFoundError:
                return []

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
