#!/usr/bin/python3
"""
a function that prints a text with 2 new lines
after each of these characters: ., ? and :
text must be a string.
"""


def text_indentation(text):
    """
    that prints a text with 2 new lines after
    each of these characters: ., ? and :
    """

    if type(text) is not str:
        raise TypeError("text must be a string")
    text = text.strip()
    a = 0
    while a < len(text):
        print(text[a], end="")
        if text[a] == "." or text[a] == "?" or text[a] == ":":
            print("\n")
            if a == len(text) - 1:
                break
            if text[a + 1] == " ":
                a = a + 1
            while text[a] == " " and text[a + 1] == " " and a + 1 < len(text):
                a = a + 1
        a = a + 1
