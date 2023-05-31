#!/usr/bin/python3
"""Class Square that defines a square"""


class Square:
    """builds a square
       finds the area"""
    def __init__(self, size=0, position=(0, 0)):
        """initializes a square of length size"""
        self.__size = size
        self.__position = position

    @property
    def size(self):
        """gets size of square"""
        return self.__size

    def position(self):
        """gets position of square"""
        return self.__position

    @size.setter
    def size(self, size):
        """sets size of square"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def position(self, value):
        """sets position of square"""
        if not isinstance(size, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = position

    def area(self):
        """ calculates area of square"""
        return self.__size ** 2

    def my_print(self):
        """prints a square using #"""
        if self.__size == 0:
            print()

        else:
            for i in range(self.__size):
                print("#" * self.__size)
