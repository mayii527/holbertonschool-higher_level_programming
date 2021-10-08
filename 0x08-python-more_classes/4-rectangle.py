#!/usr/bin/python3
"""a new class rectangle"""


class Rectangle:
    """Rectangle"""

    def __init__(self, width=0, height=0):
        """inicialite a rectangle"""
        self.width = width
        self.height = height

    @property
    def width(self):
        return(self.__width)

    @property
    def height(self):
        return(self.__height)

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """that returns the rectangle area"""
        return(self.__width * self.__height)

    def perimeter(self):
        """that returns the rectangle perimeter"""
        if self.__width == 0 or self.__height == 0:
            return(0)
        else:
            return(self.__width * 2 + self.__height * 2)

    def __str__(self):
        shape = ""
        if self.__width == 0 or self.__height == 0:
            return ""
        else:
            for col in range(self.__height):
                for row in range(self.__width):
                    shape += "#"
                if col != (self.__height - 1):
                    shape += "\n"
            return shape

    def __repr__(self):
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)
