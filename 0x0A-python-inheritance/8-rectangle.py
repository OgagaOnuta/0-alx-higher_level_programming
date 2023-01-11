#!/usr/bin/python3
"""
Creates a class Rectangle that inherits from class BaseGeometry
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ Defines a Rectangle """
    def __init__(self, width, height):
        BaseGeometry()
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
