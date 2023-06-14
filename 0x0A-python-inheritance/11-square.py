#!/usr/bin/python3
"""Function for rectangle"""

Rectangle = __import__('9-rectangle').Rectangle
"""importing another function"""


class Square(Rectangle):
    """Represent a square."""

    def __init__(self, size):
        """Initialize a new square

        Args:
            size (int): The size of the new square.
        """

        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
