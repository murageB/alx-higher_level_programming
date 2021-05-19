#!/usr/bin/python3
""" Defines a class Square """


class Square:

    """
    defines a geometric square

    Attribute:
         size (int): size of square
    """

    def __init__(self, size=0):
        """
        Initialization method

        Args:
            size (int): size of square
        Raises:
            TypeError: if size is not int
            ValueError: if size is less than 0
        """
        if type(size) != int:
            raise TypeError("size must be an interger")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """
        returns the area of the square

        Return:
            area (int) of the square
        """
        return (self.__size ** 2)

    @property
    def size(self):
        """
        gets the size attribute

        Return:
            size (int) of square

        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        set size of square to value

        Args:
            Value (int): size of a side of a square
        Raises:
            TypeError: if size is not integer
            ValueError: if size is less than 0
        Return:
            None
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def my_print(self):
        """
        Prints a square from the size using '#'

        Return:
            None
        """
        if self.__size == 0:
            print()
        else:
            for x in range(self.__size):
                print("#" * self.__size)
