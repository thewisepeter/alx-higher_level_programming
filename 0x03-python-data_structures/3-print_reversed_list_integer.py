#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    """function that prints all integers of a list, in reverse order"""
    for x in reversed(my_list):
        print("{}".format(x))
