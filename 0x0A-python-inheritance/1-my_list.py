#!/usr/bin/python3
"""
created a claas named MyList
that inherits from list
"""


class MyList(list):
    """A class named MyList"""

    def print_sorted(self):
        """prints the list, but sorted"""
        print(sorted(self))
