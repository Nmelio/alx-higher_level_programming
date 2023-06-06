#!/usr/bin/python3
# 5-text_indentation.py
"""Space"""


def text_indentation(text):
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    c = 0
    while c < len(text) and text[c] == ' ':
        c += 1

    while c < len(text):
        print(text[c], end="")
        if text[c] == "." or text[c] == ":" or text[c] == "?":
            print("\n")
            c += 2
            continue
        c += 1
