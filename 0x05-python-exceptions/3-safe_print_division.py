#!/usr/bin/python3

def safe_print_division(a, b):
    """function that divides 2 integers and prints the result"""
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        result = None
        return result
    finally:
        print("Inside result: {}".format(result))
