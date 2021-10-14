#!/usr/bin/python3
"""define a function"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """class named Square"""

    def __init__(self, size):
        self.__size = size
        self.integer_validator("size", size)

        super().__init__(size, size)
