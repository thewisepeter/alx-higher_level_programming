#!/usr/bin/python3
""" module with the class Square that is a child of Rectangle Class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """ class Square that inherits from Rectangle """

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """string representation of a Square"""
        return (f"[Square] ({self.id}) "
                f"{self.x}/{self.y} - "
                f"{self.width}"
                )
