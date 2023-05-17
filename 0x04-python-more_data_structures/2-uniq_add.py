#!/usr/bin/python3
def uniq_add(my_list=[]):
    y = 0
    x = set(my_list)

    for z in x:
        y = y + z

    return (y)
