#!/usr/bin/python3
"""2. Exact same object"""


def is_same_class(obj, a_class):
    """function that returns True or False"""
    if type(obj) == a_class:
        """if the object is exactly an instance of the specified class return True"""
        return True
    else:
        """if the object is not exactly an instance of the specified class return False"""
        return False
