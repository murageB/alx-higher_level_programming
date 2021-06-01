#!/usr/bin/python3
"""
write_file module

"""


def append_write(filename="", text=""):
    """
    appends a string at the end of  a text file (UTF8)

    Return:
        number of characters added
    """
    with open(filename, 'a', encoding="utf-8") as f:
        f.write(text)
    return len(text)
