#!/usr/bin/python3
"""module with an empty class"""


class BaseGeometry:
    """class of base geometry"""

    def area(self):
        """gets area of figure"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validates value"""
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
