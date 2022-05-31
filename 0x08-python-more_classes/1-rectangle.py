#!/usr/bin/python3
"""
1. Real definition of a rectangle
"""


class Rectangle:
    """
    Class Rectangle that defines a rectangle
    """
    def __init__(self, width=0, height=0):
        """
        Private instance attribute: width
        Private instance attribute: height
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        property to retrieve the width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        property setter to set the value of the width
        """
        if not type(value) == int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """
        property to retrieve the height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        property setter to set the value of the height
        """
        if not type(value) == int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value
