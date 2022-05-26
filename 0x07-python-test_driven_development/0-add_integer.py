#!/usr/bin/python3
"""
0. Integers addition
"""


def add_integer(a, b=98):
    """
    function that adds 2 integers
    """
    if not type(a) == int and not type(a) == float:
        """
        raise a TypeError exception if a is not interger or float
        """
        raise TypeError("a must be an integer")
    if not type(b) == int and not type(b) == float:
        """
        raise a TypeError exception if b is not interger or float
        """
        raise TypeError("b must be an integer")

    if type(a) == float:
        """
        a must be casted to integers
        """
        a = int(a)
    if type(b) == float:
        """
        a must be casted to integers
        """
        b = int(b)

    return (a + b)
