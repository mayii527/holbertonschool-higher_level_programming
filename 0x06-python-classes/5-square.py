#!/usr/bin/python3
"""define class"""


class Square:
    """constructor"""

    def __init__(self, size=0):
        """Args:
            size: the size of square
        """
        self.size = size

    @property
    def size(self):
        """return square."""
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return the area of square."""
        return (self.__size * self.__size)

    def my_print(self):
        """print the square with a #"""
        if self.__size > 0:
           for row in range(self.__size):
               for col in range(self.__size):
                   print("#", end="")
               print()
        else:
            print()
