#!/usr/bin/python3
"""
Addition Module


"""


def add_integer(a, b=98):
    """
    Adds two value of type int or float

    Args:
        a: first value passed
        b: second value passed which is intially set to 98
    Raises:
        TypeError: if a or b is not of type int or float
    Return:
        (int) : sum of a and b
    """
    if not isinstance(a, (float, int)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (float, int)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
