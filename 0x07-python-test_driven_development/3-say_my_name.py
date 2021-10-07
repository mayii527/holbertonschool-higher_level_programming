#!/usr/bin/python3
"""
function that prints My name is <first name> <last name>
first_name and last_name must be strings
otherwise, raise a TypeError exception with a message.
"""


def say_my_name(first_name, last_name=""):
    """that prints My name is <first name> <last name>"""
    if type(first_name) != str:
        raise TypeError("first_name must be a string")
    if type(last_name) != str:
        raise TypeError("last_name must be a string")
    print("My name is {:s} {:s}".format(first_name, last_name))
