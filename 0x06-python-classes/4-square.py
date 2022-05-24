#!/usr/bin/python3
"""4. Access and update private attribute"""


class Square:
    """class Square that defines a square by:(based on 3-square.py)"""

    def __init__(self, size=0):
        """raise a TypeError or ValueError exception with a message"""
        if not type(size) == int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    @property
    """property to retrieve the size"""
    def size(self):

        return self.__size

    @size.setter
    def size(self, value):
        """property setter to set the value of the size"""
        """raise a TypeError or ValueError exception with a message"""
        if not type(value) == int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """Public instance method that returns the current square area"""
        return self.__size * self.__size
