#!/usr/bin/python3
"""
a function that prints a
square with the character #.
size must be an integer.
"""


def print_square(size):
    """prints a square with the character #"""

    if type(size) != int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if type(size) is float and size < 0:
        raise TypeError("size must be an integer")
    for row in range(size):
        for col in range(size):
            print("#", end="")
        print()
