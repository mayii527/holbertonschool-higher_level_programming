#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    element = 0
    try:
       for i in range(x):
           print("{}".format(my_list[i]), end="")
           element = element + 1
    except:
        pass
    print()
    return element
