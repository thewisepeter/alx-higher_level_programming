#!/usr/bin/python3
"""module that returns a dictionary description
    of a simple data structure for JSON serialization
    of an object"""


def class_to_json(obj):
    """this function returns a dictionary description
        of a simple data structure"""
    return obj.__dict__
