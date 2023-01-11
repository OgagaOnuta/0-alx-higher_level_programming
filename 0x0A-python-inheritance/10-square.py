#!/usr/bin/python3
"""
Create a class Square that inherits from class Rectangle
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    def __init__(self, size):
        Rectangle.__init__(self, size, size)
        self.integer_validator("size", size)
        self.__size = size
        super().area()
