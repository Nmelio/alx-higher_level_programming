#!/usr/bin/python3
for num in range(0, 100):
    if num != 99:
        print("{:02}".format(number), end=", ")
    elif num == 99:
        print("{}".format(number))
