#!/usr/bin/python3
"replaces all occurrences of an element by another in a new list."
def search_replace(my_list, search, replace):
    new_list = my_list[:]
    for a in range(len(new_list)):
        if new_list[a] == search:
            new_list[a] = replace
    return (new_list)
