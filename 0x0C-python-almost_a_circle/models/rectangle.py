#!/usr/bin/python3
"""
Rectangle module

"""
from .base import Base


class Rectangle(Base):
    """
    class Rectangle - inherits from Base

    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initialisation method
        Args:
            width (int) : private attribute
            height (int) : private attribute
            x (int) : private attribute
            y (int) : private attribute
            id (int) : private attribute
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """
        width getter

        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        sets value of width
        Args:
            value (int): value to be  assigned
        Raises:
            TypeError: value must be an integer
            ValueError: value must be greater than 0
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """
        height getter

        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        sets value of height
        Args:
            value (int): value to be  assigned
        Raises:
            TypeError: value must be an integer
            ValueError: value must be greater than 0
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """
        x getter

        """
        return self.__x

    @x.setter
    def x(self, value):
        """
        sets value to x
        Args:
            value (int): value to be assigned
        Raises:
            TypeError: if value is not an integer
            ValueError: if value is < 0
        """
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """
        y getter

        """
        return self.__y

    @y.setter
    def y(self, value):
        """
        sets value to y
        Args:
            value (int): value to be assigned
        Raises:
            TypeError: if value is not an integer
            ValueError: if value is < 0
        """
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
            """
            returns the area value of the rectangle instance

            """
            return (self.__width * self.__height)

    def display(self):
        """
        prints in stdout the rectangle instance with
        the character '#'

        """
        for y in range(self.__y):
            print()
        for i in range(self.__height):
            for j in range(self.__width):
                for x in range(self.__x):
                    print("", end="")
                print("#", end="")
            print()

    def __str__(self):
        """
        returns [Rectangle](<id>)<x>/<y> - <width>/<height>

        """
        return("[Rectangle] ({}) <{}>/<{}> - <{}>/<{}>"
               .format(self.id, self.__x, self.__y,
                       self.__width, self.__height))
