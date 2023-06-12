#!/usr/bin/python3
"""module that checks if object is of specifies class"""


def is_same_class(obj, a_class):
    """function that checks if object is of specified class"""
    if isinstance(obj, a_class):
        return True
    return False
