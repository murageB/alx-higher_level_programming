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
