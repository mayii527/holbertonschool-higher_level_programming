#!/usr/bin/python3
"""
a function that writes a string to a text file
(UTF8) and returns the number of characters written
"""


def append_write(filename="", text=""):
    """appends a string at the end of a text file
    and returns the number of characters added"""

    with open(filename, 'a', encoding='utf-8') as f:
        return f.write(text)
