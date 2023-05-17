#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    e = list(a_dictionary.keys())

    for f in e:
        if value == a_dictionary.get(f):
            del a_dictionary[f]

    return (a_dictionary)
