#!/usr/bin/python3
"""module that prints a square with the character #"""


def print_square(size):
    """function that prints a square with the character #"""
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise TypeError("size must be >= 0")
    if isinstance(size, float) and size > 0:
        raise TypeError("size must be an integer")

    for _ in range(size):
        print('#' * size)
