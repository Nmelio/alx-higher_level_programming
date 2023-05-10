#!/usr/bin/python3
for num_1 in range(0, 10):
    for num_2 in range(num_1 + 1, 10):
        if num_1 != 8:
            print("{}{}".format(num_1, num_2), end= ", ")
        elif num_1 == 8:
            print("{}{}".format(num_1, num_2))
