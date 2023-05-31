#!/usr/bin/python3
"""Class Square that defines a square"""


class Square:
    """builds a square
       finds the area"""
    def __init__(self, size=0):
        """initializes a square of length size"""
        self.__size = size

    @property
    def size(self):
        """gets size of square"""
        return self.__size

    @size.setter
    def size(self, size):
        """sets size of square"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """ calculates area of square"""
        return self.__size ** 2
