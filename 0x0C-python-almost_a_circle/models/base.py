#!/usr/bin/python3
"""
Base module

"""


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
    
