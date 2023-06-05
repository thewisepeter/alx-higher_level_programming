#!/usr/bin/python3

class Rectangle:
    """ Rectangle Definition"""
    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """get width"""
        return self.__width

    @width.setter
    def width(self, width):
        """ sets width """
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        self.__width = width


