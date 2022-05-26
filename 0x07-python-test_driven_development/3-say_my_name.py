#!/usr/bin/python3
"""
2. Say my name
"""


def say_my_name(first_name, last_name=""):
    """
    Function that prints: My name is <first name> <last name>
    """
    if not type(first_name) == str:
        """
        raise a TypeError exception if first_name is not a string
        """
        raise TypeError("first_name must be a string")
    if not type(last_name) == str:
        """
        raise a TypeError exception if last_name is not a string
        """
        raise TypeError("last_name must be a string")
    else:
        print("My name is %s %s" % (first_name, last_name))
