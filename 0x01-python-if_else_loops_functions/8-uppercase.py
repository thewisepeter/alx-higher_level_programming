#!/usr/bin/python3
def uppercase(str):
    """prints a string in uppercase"""
    for char in str:
        if ord(char) in range(97, 123):
            print("{}".format(chr(ord(char) - 32)), end="")
        elif ord(char) in range(65, 91):
            print("{}".format(char), end="")
        else:
            print("{}".format(char), end="")
    print()
