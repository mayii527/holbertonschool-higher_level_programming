#!/usr/bin/python3
"""
define the function def inherits_from(obj, a_class)
"""


def inherits_from(obj, a_class):
    """return true or false of a class that inherited"""

    if isinstance(obj, a_class) != a_class:
        return True
    else:
        return False
