#!/usr/bin/python3
"""
a function that writes a string to a text file
(UTF8) and returns the number of characters written
"""


def append_write(filename="", text=""):
    with open(filename, 'a', encoding='utf-8') as f:
        return f.write(text)