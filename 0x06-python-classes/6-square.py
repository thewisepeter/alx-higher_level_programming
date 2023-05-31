#!/usr/bin/python3
"""Class Square that defines a square"""


class Square:
    """builds a square
       finds the area"""

    def __init__(self, size=0, position=(0, 0)):
        """initializes a square of length size"""

        self.__size = size
        self.__position = position

    def __str__(self):
        self.my_print()

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

    @property
    def position(self):
        """gets position of square"""

        return self.__position

    @position.setter
    def position(self, value):
        """sets position of square"""

        if (not isinstance(value, tuple) or len(value) != 2 or not
                all(isinstance(num, int) for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """ calculates area of square"""

        return self.__size ** 2

    def pos_print(self):
        """ gets position in spaces"""
        pos = ""

        if self.__size == 0:
            return "\n"
        for w in range(self.__position[1]):
            pos += "\n"
        for w in range(self.__size):
            for i in range(self.position[0]):
                pos += " "
            for j in range(self.position[0]):
                pos += "#"
            pos += "\n"
        return pos

    def my_print(self):
        """prints a square using #"""
        print(self.pos_print(), end="")
