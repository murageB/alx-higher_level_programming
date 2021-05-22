#!/usr/bin/python3
"""

Say_my_name module

"""


def say_my_name(first_name, last_name=""):
    """
    print full name

    Args:
        first_name: first string passed
        last_name: secong string passed

    Raises:
        TypeError: if first_name and last_name are not strings

    Return: None
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {:s} {:s}".format(first_name, last_name))
