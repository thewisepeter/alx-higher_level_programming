#!/usr/bin/python3
"""module of the class Base"""


class Base:
    """this is the base class from which others inherit"""
    __nb_objects = 0

    def __init__(self, id=None):
        """ initiation method
        args:
            id
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
