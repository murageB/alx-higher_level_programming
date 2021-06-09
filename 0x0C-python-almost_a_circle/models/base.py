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
        list_f = []
        with open(cls.__name__ + ".json", encoding="utf-8") as f:
            if list_objs:
                for obj in list_objs:
                    list_f.append(obj.to_dictionary())
            f.write(cls.to_json_string(list_f))
