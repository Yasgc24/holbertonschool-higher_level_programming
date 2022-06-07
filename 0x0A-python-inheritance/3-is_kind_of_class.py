#!/usr/bin/python3
"""3. Same class or inherit from"""


def is_kind_of_class(obj, a_class):
    """function that returns True or Flase"""
    if isinstance(obj, a_class):
        """if the object is an instance of, or is an instance
        of a class that inherited from return True"""
        return True
    else:
        """if the object is not an instance of, or is not an instance
        of a class that inherited from return False"""
        return False
