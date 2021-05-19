#!/usr/bin/python3
""" Defines a class Square """


class Square:

    """
    defines a geometric square

    Attribute:
         size (int): size of square
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Initialization method

        Args:
            size (int): size of square
            position (tuple): position of square in 2D space
        """
        self.__size = size
        self.__position = position

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

    @property
    def position(self):
        """
        gets the position of square in 2D space

        Return:
            position of square
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
            sets position
        Args:
            value (tuple): position of the square in 2D space
        Return:
            None
        """
        if len(value) != 2 or type(value) != tuple:
            raise TypeError("position must be a tuple of 2 positive integers")
        if type(value[0]) != int or value[0] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        if type(value[1]) != int or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def my_print(self):
        """
        Prints a square from the size using '#'

        Return:
            None
        """
        if self.__size == 0:
            print()
        else:
            print("\n" * self.__position[1], end='')
            for x in range(self.__size):
                print(" " * self.__position[0], end='')
                print("#" * self.__size)
