#!/usr/bin/python3
"""
Print square module


"""


def print_square(size):
    """
    Prints square using "#"

    Args:
        size: size of one side of the square
    Raises:
        TypeError: if size is not integer
        ValueErro: if size is less than 0
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if type(size) is float and size < 0:
        raise TypeError("size must be an integer")
    for x in range(size):
        print("#" * size)
