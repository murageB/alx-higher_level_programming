#!/usr/bin/python3
"""
write_file module

"""


def write_file(filename="", text=""):
    """
    writes a string to a text file (UTF8)

    Return:
        number of characters written
    """
    with open(filename, 'w', encoding="utf-8") as f:
        f.write(text)
    return len(text)
