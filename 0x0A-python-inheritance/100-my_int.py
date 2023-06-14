#!/usr/bin/python3
"""module with class that inherits from int"""


class MyInt(int):
    """rebel class that inherits from int
    inverts == and !=
    pure evil!!!!"""
    def __eq__(self, other):
        """reverses =="""
        return super().__ne__(other)

    def __ne__(self, other):
        """reverses !="""
        return super().__eq__(other)
