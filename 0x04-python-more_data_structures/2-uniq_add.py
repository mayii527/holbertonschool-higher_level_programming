#!/usr/bin/python3
"res = result"
def uniq_add(my_list=[]):
    res = 0
    for x in set(my_list):
        res = res + x
    return (res)
