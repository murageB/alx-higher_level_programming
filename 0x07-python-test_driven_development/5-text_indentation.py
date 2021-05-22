#!/usr/bin/python3
"""

Text Indentation module

"""


def text_indentation(text):
    """

    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    a = 0
    while a < len(text):
        if text[a] in ["?", ".", ":"]:
            print(text[a])
            print()
            a += 1
        else:
            print(text[a], end='')
        a += 1
