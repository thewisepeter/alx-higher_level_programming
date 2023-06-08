#!/usr/bin/python3
""" module that only initiates first_name"""


class LockedClass:
    def __init__(first_name):
        """ only initiates first_name """
        __slots__ = ["first_name"]
