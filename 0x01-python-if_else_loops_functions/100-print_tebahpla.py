#!/usr/bin/python3
for x in range(90, 64, -1):
    if (x % 2 == 0):
        x += 32
    print("{}".format(chr(x)), end="")
