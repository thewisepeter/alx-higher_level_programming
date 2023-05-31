#!/usr/bin/python3
"""Class Square that defines a square"""


class Square:
    """builds a square
       finds the area"""
    def __init__(self, size=0):
        """initializes a square of length size"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        return self.__size ** 2
