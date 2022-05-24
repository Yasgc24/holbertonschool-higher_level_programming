#!/usr/bin/python3
"""6. Coordinates of a square"""


class Square:
    """class Square that defines a square by:(5-square.py)"""
    def __init__(self, size=0, position=(0, 0)):
        """raise a TypeError or ValueError exception with a message"""
        if not type(size) == int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

        """raise a TypeError exception with a message"""
        if not type(position) == tuple or not len(position) == 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not type(position[0]) == int or not type(position[1]) == int:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif position[0] < 0 or position[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = position

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

    @property
    def position(self):
        """property to retrieve the position"""
        return self.__position

    @position.setter
    def position(self, value):
        """property setter to set the value of the position"""
        """raise a TypeError exception with a message"""
        if not type(value) == tuple or not len(value) == 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not type(value[0]) == int or not type(value[1]) == int:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__value = value

    def area(self):
        """Public instance method that returns the current square area"""
        return self.__size * self.__size

    def my_print(self):
        """Public instance method that prints in stdout
        the square with the character #"""
        if self.__size == 0:
            print()
        else:
            print("\n" * self.__position[1], end="")
            for i in range(self.__size):
                print(" " * self.__position[0], end="")
                for i in range(self.__size):
                    print('#', end="")
                print()
