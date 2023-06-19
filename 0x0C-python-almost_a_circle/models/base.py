#!/usr/bin/python3
"""module of the class Base"""
import json

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

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the JSON string representation of list_dictionaries"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes the JSON string representation of list_objs to a file."""
        if list_objs is None:
            list_objs = []

        file_name = cls.__name__ + ".json"
        json_data = cls.to_json_string([obj.to_dictionary()
                                        for obj in list_objs])

        with open(file_name, "w") as a_file:
            a_file.write(json_data)
