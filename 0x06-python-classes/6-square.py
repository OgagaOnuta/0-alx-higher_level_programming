#!/usr/bin/python3
'''
Creates a class Square that defines a square
'''


class Square:
    '''
    Defines a square
    '''
    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

    @property
    def size(self):
        return (self.__size)

    @size.setter
    def size(self, value):
        self.__size = value
        if (type(self.__size) is not int):
            raise TypeError("size must be an integer")
        if (self.__size < 0):
            raise ValueError("size must be >= 0")

    @property
    def position(self):
        return (self.__position)

    @position.setter
    def position(self, value):
        self.__position = value
        if ((self.__position[0] < 0) or (self.__position[1] < 0)):
            raise TypeError("position must be a tuple of 2 positive integers")

    def area(self):
        return (self.__size * self.__size)

    def my_print(self):
        if (self.__size == 0):
            print()
        else:
            for i in range(self.__size):
                print(" " * self.__position[0], end="")
                print("#" * self.__size)
