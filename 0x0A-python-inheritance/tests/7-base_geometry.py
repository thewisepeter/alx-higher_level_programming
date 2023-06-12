The ''7-base_geometry'' module
==============================

integer_validator that validates value
--------------------------------------

Using integer_validator
-----------------------

import BaseGeometry class from ''7-base_geometry'' module
    >>> big_geo = __import__('7-base_geometry').BaseGeometry

checking for area
    >>> figure = big_geo()
    >>> figure.area()
    Traceback (most recent call last):
        ...
    Exception: area() is not implemented

1 argument to area
    >>> figure.area(2)
    Traceback (most recent call last):
        ...
    TypeError: BaseGeometry.area() takes 1 positional argument but 2 were given

checking integer_validator with positive integer
    >>> figure.integer_validator("Peter", 1)

checking integer_validator with 0
    >>> figure.integer_validator("Peter", 0)
    Traceback (most recent call last):
        ...
    ValueError: Peter must be greater than 0

checking integer_validator with negative integer
    >>> figure.integer_validator("Peter", -3)
    Traceback (most recent call last):
        ...
    ValueError: Peter must be greater than 0

checking integer_validator with string
    >>> figure.integer_validator("Peter", "string")
    Traceback (most recent call last):
        ...
    TypeError: Peter must be an integer

checking integer_validator with float
    >>> figure.integer_validator("Peter", 2.3)
    Traceback (most recent call last):
        ...
    TypeError: Peter must be an integer
