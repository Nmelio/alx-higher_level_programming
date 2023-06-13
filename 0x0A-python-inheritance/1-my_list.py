#!/usr/bin/python3
"""Defines an inherited list"""


class MyList(list):
    """sorted printing"""

    def print_sorted(self):
        """Print ascending order."""
        print(sorted(self))
