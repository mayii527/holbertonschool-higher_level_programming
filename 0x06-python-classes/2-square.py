#!/usr/bin/python3
"""define class"""


class Square:
    """constructor"""

    def __init__(self, size=0):
        """Args:
        size: the size of the square
        """
        self.__size = size
        if size is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
