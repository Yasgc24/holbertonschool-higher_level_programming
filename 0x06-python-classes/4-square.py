#!/usr/bin/python3
"""4. Access and update private attribute"""


class Square:
    """class Square that defines a square by:
    (based on 3-square.py)"""

    def __init(self, size=0):
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            sielf.__size = value

    def area(self):
        return self.__size * self.__size
