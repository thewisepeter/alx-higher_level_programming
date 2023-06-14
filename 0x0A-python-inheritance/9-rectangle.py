#!/usr/bin/python3
"""module with Recatangle class that inherits from BaseGeometry"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle child"""
    def __init__(self, width, height):
        """initiates rectangle"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """returns area of rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """returns string representation of Rectangle"""
        string = "[" + str(self.__class__.__name__) + "]"
        string += str(self.__width) + "/" + str(self.__height)
        return string
