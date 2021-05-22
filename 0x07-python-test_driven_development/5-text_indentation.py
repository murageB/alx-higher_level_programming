#!/usr/bin/python3
"""

Text Indentation module

"""


def text_indentation(text):
    """
    prints a text with 2 new lines after 
    each of these characters: ., ? and :

    Args:
       text (str): text to be split 
    Raise:
        TypeError: when text is not str
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
