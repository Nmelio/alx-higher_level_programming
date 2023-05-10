#!/usr/bin/python3
def pow(a, b):
#    x = a**b
#    return x
    x = a
    for y in range(0,b):
        x *= a
    return x
