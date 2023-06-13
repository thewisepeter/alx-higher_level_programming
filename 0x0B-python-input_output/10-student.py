#!/usr/bin/python3
""" this is a module with a  student class"""


class Student:
    """this is a student class"""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """returns dictionary representation of Student"""
        if attrs is None:
            return self.__dict__
        return {attr: getattr(self, attr) for attr in
                attrs if hasattr(self, attr)}
