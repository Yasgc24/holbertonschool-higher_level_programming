#!/usr/bin/python3
"""
3. Print square
"""


def print_square(size):
    """
    Function that prints a square with the character #
    ------
    size: size length of the square
    """
    if not type(size) == int:
        """
        raise a TypeError exception if size is not a interger
        """
        raise TypeError("size must be an integer")
    if size < 0:
        """
        raise a ValueError exception if size is less than 0
        """
        raise ValueError("size must be >= 0")
    else:
        for i in range(size):
            print('#' * size)
