#!/usr/bin/python3
"""module with class MyList that inherits from list"""


class MyList(list):
    """class MyList that inherits from list"""

    def print_sorted(self):
        """prints sorted list"""
        print(sorted(self))
