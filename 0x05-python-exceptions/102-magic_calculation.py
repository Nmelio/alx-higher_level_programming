#!/bin/usr/python3

def magic_calculation(a, b):
    t = 0
    for u in range(1, 3):
        try:
            if u > a:
                raise Exception('Too far')
            else:
                t += a ** b / u
        except:
            t = b + a
            break
        return (t)
