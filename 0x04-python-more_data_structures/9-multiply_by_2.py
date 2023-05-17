#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    m = a_dictionary.copy()
    n = list(m.keys())
    for o in n:
        m[o] *= 2

    return (m)
