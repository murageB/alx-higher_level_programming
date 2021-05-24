#!/usr/bin/python3
"""

Rectangle module

"""


class Rectangle:
    """
    Defines a rectangle

    Args:
        width (int): private
        height (int): private
    """
    def __init__(self, width=0, height=0):
        """
        Defines a rectangle

        Args:
            width (int): width of the rectangle
            height (int): height of the rectangle
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        Gets width of the rectangle

        Return:
            width (int) of thr rectange
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        sets value to width

        Args:
            value (int): value to be set to width
        Raises:
            TypeError: if value is not an integer
            ValueError: if value is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value
    
    @property
    def height(self):
        """
        gets height

        Return:
            height (int) of the retangle
        """
        return self.__height

    @width.setter
    def height(self, value):
        """
        sets value to height

        Args:
            value (int): value to be set to height
        Raises:
            TypeError: if value is not an integer
            ValueError: if value is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
