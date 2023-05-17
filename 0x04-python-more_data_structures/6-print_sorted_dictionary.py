#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    y = list(a_dictionary.keys())
    y.sort()
    for x in y:
        print("{}: {}".format(x, a_dictionary.get(x)))
