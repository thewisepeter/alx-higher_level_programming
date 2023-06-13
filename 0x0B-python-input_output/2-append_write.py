#!/usr/bin/python3
"""module that appends a string to a text file
   Return: number of characters written"""


def append_write(filename="", text=""):
    """appends a string to a text file"""
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
