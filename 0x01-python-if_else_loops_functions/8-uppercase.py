#!/usr/bin/python3
def uppercase(str):
    """prints a string in uppercase"""
    for char in str:
        if ord(char) in range(97, 123):
            char = chr(ord(char) - 32)
        print("{}".format(char), end="")
    print("")
