#!/usr/bin/python3
"""
Base module

"""
import json


class Base:
    """
    Base class
    Attributes:
        __nb_objects: private class attribute
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initialization method
        Args:
           id
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Returns the JSON string representation of list_dictionaries

        """
        if list_dictionaries is None:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        writes the JSON string representation of list_objs to a file

        """
        list_f = [obj.to_dictionary() for obj in list_objs]
        filename = [obj.__class__.__name__ for obj in list_objs][0] + '.json'
        with open(filename,'w', encoding="utf-8") as f:
            return f.write(cls.to_json_string(list_f))

    @staticmethod
    def from_json_string(json_string):
        """
        returns the list of the JSON string representation json_string

        """
        if json_string == "" or json_string is None:
            return []
        return json.loads(json_string)
