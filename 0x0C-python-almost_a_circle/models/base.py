#!/usr/bin/python3
""" module with the base class"""


class Base:
    """base of all other classes
        prevents code duplication
        and by extension bugs"""

    __nb_objects = 0

    def __init__(self, id=None):
        """ initialises the Base """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
