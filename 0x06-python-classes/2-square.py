#!/usr/bin/python3
"""2. Size validation"""


class Square:
    """class Square that defines a square
    by:(based on 1-square.py) with exception
    with the message"""
    def __init__(self, size=0):
        if not type(size) == int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
