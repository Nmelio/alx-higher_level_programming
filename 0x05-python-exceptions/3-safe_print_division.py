#!/usr/bin/python3

def safe_print_division(a, b):
    try:
        c = a/b
    except (ZeroDivisionError, ValueError, TypeError):
        print(end="")
    finally:
        print("{}".format(c), end="")
