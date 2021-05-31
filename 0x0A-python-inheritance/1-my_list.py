#!/usr/bin/python3
"""
MyList module
"""


class MyList(list):
    """
    inherits from list
    """
    def print_sorted(self):
        """
        prints sorted list
        """
        print(sorted(self))
