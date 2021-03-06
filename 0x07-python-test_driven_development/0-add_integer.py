#!/usr/bin/python3
"""
a function that adds 2 integers.
a and b must be integers or floats.
Returns an integer.
"""


def add_integer(a, b=98):
    """add of two integers"""
    if(type(a) != int and type(a) != float):
        raise TypeError("a must be an integer")
    if(type(b) != int and type(b) != float):
        raise TypeError("b must be an integer")
    if(type(a) is float):
        a = int(a)
    if(type(b) is float):
        b = int(b)
    return a+b
