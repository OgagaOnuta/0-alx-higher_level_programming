#!/usr/bin/python3
"""Create a class Square that inherits from class Rectangle"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    def __init__(self, size):
        self.integer_validator("size", size)
        self.__size = size
        Rectangle.__init__(self, self.__size, self.__size)
        super().area()

    def __str__(self):
        return ("[Square] {0}/{0}".format(self.__size))
