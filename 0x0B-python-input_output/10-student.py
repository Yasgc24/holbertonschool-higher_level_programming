#!/usr/bin/python3
"""10. Student to JSON with filter"""


class Student:
    """class Student that defines a student"""
    def __init__(self, first_name, last_name, age):
        """Instantiation with public instance attributes"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Public method  that retrieves a dictionary
        representation of a instance
        ----------------
        If attrs is a list of strings, only attribute names
        contained in this list must be retrieved
        ----------------
        Otherwise, all attributes must be retrieved"""
        my_dic = {}
        if attrs is None:
            return self.__dict__

        for i in attrs:
            if hasattr(self, i):
                my_dic[i] = getattr(self, i)
        return my_dic
