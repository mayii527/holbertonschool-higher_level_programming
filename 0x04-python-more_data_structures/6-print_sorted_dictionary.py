#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    [print("{}: {}".format(k, a_dictionary)) for k in sorted(a_dictionary)]
