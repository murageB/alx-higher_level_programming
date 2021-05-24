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

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """
        Defines a rectangle

        Args:
            width (int): width of the rectangle
            height (int): height of the rectangle
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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

    def area(self):
        """
        return the area of the rectangle

        Return:
            Area (int) of the rectangle
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        return the perimeter of the rectangle

        Return:
            perimeter (int) of the rectangle
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width * 2) + (self.__height * 2)

    def __str__(self):
        """
        Prints rectangle using #

        Return:
            printed rectangle using #
        """
        if self.__width == 0 or self.__height == 0:
            return ""
        symb = str(self.print_symbol)
        return ((symb*self.__width + "\n")*self.__height)[:-1]

    def bigger_or_equal(rect_1, rect_2):
        """
        compares two rectangles
        Args:
            rect_1 (Rectangle): first rectangle
            rect_2 (Rectangle): second rectangle
        Raises:
            TypeError: if not an instance of Rectangle
        Return:
            the biggest rectangle based on area
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        Area1 = rect_1.area()
        Area2 = rect_2.area()
        if Area1 >= Area2:
            return rect_1
        return rect_2

    def __repr__(self):
        """
        string representation of the rectangle

        Return:
            (str) representation of the rectangle
        """
        return ("Rectangle({}, {})".format(self.__width, self.__height))

    def __del__(self):
        """
        Print the message when an instance of Rectangle is deleted

        """
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
