#!/usr/bin/python3
"""9. Student to JSON"""


class Student:
    """class Student that defines a student"""
    def __init__(self, first_name, last_name, age):
        """Instantiation with public instance attributes"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Public method  that retrieves a dictionary
        representation of a instance"""
        return self.__dict__
