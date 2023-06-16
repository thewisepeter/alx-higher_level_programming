#!/usr/bin/python3
""" module with the class Rectangle that inherits from Base"""
from models.base import Base


class Rectangle(Base):
    """ Rectangle that inherits from Base """

    def __init__(self, width, height, x=0, y=0, id=None):
        """initialises Rectangle"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width):
        self.__width = width

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        self.__height = height

    @property
    def x(self):
        return x

    @x.setter
    def x(self, x):
        self.__x = x

    @property
    def y(self):
        return y

    @y.setter
    def y(self, y):
        self.__y = y
