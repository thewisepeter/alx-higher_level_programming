#!/usr/bin/python3
"""this module creates an Object from a JSON file"""
import json


def load_from_json_file(filename):
    """this function function that creates
        an Object from a JSON file"""
    with open(filename, encoding='utf=8') as f:
        x = json.load(f)
