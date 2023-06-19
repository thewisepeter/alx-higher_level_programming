#!/usr/bin/python3
"""module with Rectangle class that inherits from Base"""
from models.base import Base


class Rectangle(Base):
    """class Rectangle that inherits from Base"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """ initializes Rectangle
        args:
            width: rectangle width
            height: rectangle height
            x: coordinate
            y: coordinate
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """returns the rectangle width"""
        return self.__width

    @width.setter
    def width(self, width):
        """initializes rectangle width"""
        if type(width) is not int:
            raise TypeError("width must be an integer")
        elif width <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = width

    @property
    def height(self):
        """returns the rectangle height"""
        return self.__height

    @height.setter
    def height(self, height):
        """initializes rectangle height"""
        if type(height) is not int:
            raise TypeError("height must be an integer")
        elif height <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = height

    @property
    def x(self):
        """returns x cordinate"""
        return self.__x

    @x.setter
    def x(self, x):
        """initializes x coordiante"""
        if type(x) is not int:
            raise TypeError("x must be an integer")
        elif x < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = x

    @property
    def y(self):
        """ returns y coordinate """
        return self.__y

    @y.setter
    def y(self, y):
        """initializes y cordinate"""
        if type(y) is not int:
            raise TypeError("y must be an integer")
        elif y < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = y

    def area(self):
        """returns the area of the rectangle"""
        return self.__width * self.__height

    def display(self):
        """displays the rectangle using #"""
        print("\n" * self.__y, end="")
        for x in range(self.__height):
            print(" " * self.__x + "#" * self.__width)

    def __str__(self):
        """string representation of the rectangle"""
        return (f"[Rectangle] ({self.id}) "
                f"{self.__x}/{self.__y} - "
                f"{self.__width}/{self.__height}"
                )

    def update(self, *args, **kwargs):
        """updates attributes of rectangle"""
        if args:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.__width = args[1]
            if len(args) >= 3:
                self.__height = args[2]
            if len(args) >= 4:
                self.__x = args[3]
            if len(args) >= 5:
                self.__y = args[4]

        elif kwargs and len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                elif key == "width":
                    self.__width = value
                elif key == "height":
                    self.__height = value
                elif key == "x":
                    self.__x = value
                elif key == "y":
                    self.__y = value
