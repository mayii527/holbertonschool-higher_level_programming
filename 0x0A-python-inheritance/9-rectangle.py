#!/usr/bin/python3
"""define class"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """class named Rectangle"""

    def __init__(self, width, height):
        """initiation instance"""

        self.__width = width
        self.__height = height
        self.integer_validator("width", width)
        self.integer_validator("height", height)

    def area(self):
        """return area"""

        return self.__width * self.__height
