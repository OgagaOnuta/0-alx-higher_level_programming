#!/usr/bin/python3
"""
Creates a class that defines a rectangle
"""


class Rectangle:
    """Defines a rectangle"""
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        return (self.__width)

    @width.setter
    def width(self, value):
        self.__width = value
        if (type(self.__width) is not int):
            raise TypeError("width must be an integer")
        if (self.__width < 0):
            raise ValueError("width must be >= 0")

    @property
    def height(self):
        return (self.__height)

    @height.setter
    def height(self, value):
        self.__height = value
        if (type(self.__height) is not int):
            raise TypeError("height must be an integer")
        if (self.__height < 0):
            raise ValueError("height must be >= 0")
