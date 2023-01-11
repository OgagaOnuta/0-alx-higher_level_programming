#!/usr/bin/python3
"""
Creates a class that defines a student
"""


class Student:
    """ Defines a student """
    def __init__(self, first_name, last_name, age):
        """ Instantiates a Student object """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """ Retrieves a dictionary representation """
        return (self.__dict__)
