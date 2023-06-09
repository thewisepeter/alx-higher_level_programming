#!/usr/bin/python3
"""This is a  module that writes an Object to a
    text file in JSON representation"""

import json


def save_to_json_file(my_obj, filename):
    """this function writes an Object to a
        text file in JSON representation"""
    with open(filename, 'w') as f:
        json.dump(my_obj, f)
