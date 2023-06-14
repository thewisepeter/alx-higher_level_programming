#!/usr/bin/python3
"""module that adds a new attribute to an object if it’s possible"""


def add_attribute(obj, attr, value):
    """adds new attibute to an object if possible"""
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")

    obj.__dict__[attr] = value
