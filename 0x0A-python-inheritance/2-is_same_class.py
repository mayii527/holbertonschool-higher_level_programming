#!/usr/bin/python3
"""
define class def is_same_class(obj, a_class)
"""


def is_same_class(obj, a_class):
    """ returns True if the object
    is exactly an instance,
    otherwise False."""

    return type(obj) == a_class
