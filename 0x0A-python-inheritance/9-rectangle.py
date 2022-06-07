#!/usr/bin/python3
"""8. Rectangle"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Write a class Rectangle that inherits from BaseGeometry (7-base_geometry.py)(task based on 8-rectangle.py)"""
    def __init__(self, width, height):
        """Instantiation with width and height
        width and height must be private and must be
        positive integers, validated by integer_validator
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        return self.__width * self.__height 

    def __str__(self):
        return ("[Rectangle] {}/{}".format(self.__width, self.__height))