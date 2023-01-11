#!/usr/bin/python3
"""
Creates a class Rectangle that inherits from class BaseGeometry
"""


class BaseGeometry:
    """ A Base Geometry class """
    def __init__(self):
        pass

    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if (type(value) is not int):
            raise TypeError("{} must be an integer".format(name))
        if (value <= 0):
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """ Defines a Rectangle """
    def __init__(self, width, height):
        BaseGeometry()
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
