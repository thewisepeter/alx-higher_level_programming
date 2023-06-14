#!/usr/bin/python3
"""module with square class"""
Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """Square child"""
    def __init__(self, size):
        """initiates square"""
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        return self.__size * self.__size

    def __str__(self):
        return f"[Square] {self.__size}/{self.__size}"
