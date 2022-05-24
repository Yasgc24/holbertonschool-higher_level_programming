#!/usr/bin/python3
"""5. Printing a square"""


class Square:
    """class Square that defines a square by:(4-square.py)"""
    def __init__(self, size=0):
        if not type(size) == int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    @property
    def size(self):
        """property to retrieve the size"""
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

    def my_print(self):
        """Public instance method that prints in stdout
        the square with the character #"""
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                print('#' * self.__size)


    
