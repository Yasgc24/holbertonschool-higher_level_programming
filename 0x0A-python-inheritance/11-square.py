#!/usr/bin/python3
"""11. Square #2"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Write a class Square that inherits from Rectangle (9-rectangle.py)
    (task based on 10-square.py)"""
    def __init__(self, size):
        """Instantiation with size"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """returns the area of the square"""
        return (self.__size * self.__size)

    def __str__(self):
        """should return, the square description"""
        return (("[Square] {}/{}".format(self.__size, self.__size)))
