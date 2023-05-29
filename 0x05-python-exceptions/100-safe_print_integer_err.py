#!/usr/bin/python3
import sys

def safe_print_integer_err(value):
    """function that prints an integer"""
    try:
        print("{:d}".format(value))
        return True
    except (ValueError, TypeError):
        print("Exception:")
        return False
