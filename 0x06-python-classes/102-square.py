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
    def size(self, value):
        """sets size of square"""
        if not isinstance(value, (int, float)):
            raise TypeError("size must be a number")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """ calculates area of square"""
        return self.__size ** 2

    def __eq__(self, other):
        return self.area() == other.area()

    def __ne__(self, other):
        return self.area() != other.area()

    def __lt__(self, other):
        return self.area() < other.area()

    def __le__(self, other):
        return self.area() <= other.area()

    def __gt__(self, other):
        return self.area() > other.area()

    def __ge__(self, other):
        return self.area() >= other.area()
