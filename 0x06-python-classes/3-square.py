#!/usr/bin/python3
"""3. Area of a square"""


class Square:
    """class Square that defines a square by:
    (based on 2-square.py)"""
    def __init__(self, size=0):
        """raise a TypeError or ValueError exception with a message"""
        if not type(size) == int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """Public instance method that returns the current square area"""
        return self.__size * self.__size
