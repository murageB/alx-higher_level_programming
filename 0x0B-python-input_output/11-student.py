#!/usr/bin/python3
"""
Student module

"""


class Student:
    """
    define a student
    Attributes:
        first_name
        last_name
        age
    """
    def __init__(self, first_name, last_name, age):
        """
        initialization method

        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        retrieves a dictionary representation of a Student instance
        """
        if isinstance(attrs, list) and all(
                isinstance(s, str) for s in attrs):
            return{i: j for i, j in self.__dict__.items() if i in attrs}
        return self.__dict__

    def reload_from_json(self, json):
        """
        replaces all attributes of the Student instance
        """
        for key, value in json.items():
            if hasattr(self, key):
                setattr(self, key, value)
