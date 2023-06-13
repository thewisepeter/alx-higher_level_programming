#!/usr/bin/python3
""" this is a module with a  student class"""


class Student:
    """this is a student class"""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """returns dictionary representation of Student"""
        return self.__dict__
