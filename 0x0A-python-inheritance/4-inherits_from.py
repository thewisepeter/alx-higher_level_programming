#!/usr/bin/python3
"""module that returns True if object is an instance inherited
    from specified class"""


def inherits_from(obj, a_class):
    """function that checks if the object is an instance
    of a class that inherited (directly or indirectly)
    from the specified class"""
    return issubclass(type(obj), a_class) and type(obj) != a_class
