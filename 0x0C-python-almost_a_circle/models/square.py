#!/usr/bin/python3
"""
Square module

"""
from .rectangle import Rectangle


class Square(Rectangle):
    """
    Defines square class
    Attr:
        size(int): size of square
        x(int): value at x axis
        y(int): value at y axis
        id(int): identifies square instance
    """
    def __init__(self, size, x=0, y=0, id=None):
        """
        initializes all attributes of the square instance

        """

        super().__init__(size, size, x, y, id)
        self.size = size

    @property
    def size(self):
        """
        get size
        """
        return self.__width

    @size.setter
    def size(self, value):
        """
        sets value to size
        Attr:
            value(int): value to be set to size
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value
        self.__height = value

    def __str__(self):
        """
        string representation of the square

        """
        return "[Square] ({:d}) {:d}/{:d} - {:d}".format(self.id, self.x,
                                                         self.y, self.size)

    def update(self, *args, **kwargs):
        """
        updates Square instance

        """
        i=0
        if args:
            for arg in args:
                if i == 0:
                    self.id = arg
                elif i == 1:
                    self.size = arg
                elif i == 2:
                    self.x = arg
                elif i == 3:
                    self.y = arg
                i += 1
        else:
            for arg in kwargs:
                setattr(self, arg, kwargs.get(arg))
