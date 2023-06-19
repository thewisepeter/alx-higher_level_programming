#!/usr/bin/python3
"""module with Rectangle class that inherits from Base"""
from models.base import Base


class Rectangle(Base):
    """class Rectangle that inherits from Base"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """ initializes Rectangle
        args:
            width: rectangle width
            height: rectangle height
            x: coordinate
            y: coordinate
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """returns the rectangle width"""
        return self.__width

    @width.setter
    def width(self, value):
        """initializes rectangle width"""
        self.__width = value

    @property
    def height(self):
        """returns the rectangle height"""
        return self.__height

    @height.setter
    def height(self, height):
        """initializes rectangle height"""
        self.__height = height

    @property
    def x(self):
        """returns x cordinate"""
        return self.__x

    @x.setter
    def x(self, x):
        """initializes x coordiante"""
        self.__x = x

    @property
    def y(self):
        """ returns y coordinate """
        return self.__y

    @y.setter
    def y(self, y):
        """initializes y cordinate"""
        self.__y = y
