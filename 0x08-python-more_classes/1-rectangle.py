#!/usr/bin/python3
"""a new class rectangle"""


class Rectangle:
    """Rectangle"""

    def __init__(self, width=0, height=0):
        """inicialite a rectangle"""
        self.__width = width
        self.__height = height

    @property
    def width(self):
        return(self.width)

    @property
    def height(self):
        return(self.height)

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
