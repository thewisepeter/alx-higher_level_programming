#!/usr/bin/python3
""" module with the base class"""
import json

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

    def to_json_string(list_dictionaries):
        """returns the JSON string representation of list_dictionaries"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)
