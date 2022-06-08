#!/usr/bin/python3
"""7. Integer validator"""


class BaseGeometry:
    """Write a class BaseGeometry (based on 6-base_geometry.py)"""
    def area(self):
        """Public instance method that raises an Exception with a message"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Public instance method that validates the value"""
        if not type(name) == str:
            return
        if not type(value) == int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
