#!/usr/bin/python3
"""Creates a class that defines a rectangle"""


class Rectangle:
    """Defines a rectangle"""
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initialize an instance of class Rectangle"""
        self.width = width
        self.height = height
        type(self).number_of_instances += 1

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

    def area(self):
        """Returns the area of a rectangle"""
        return (self.__width * self.__height)

    def perimeter(self):
        """Returns the perimeter of a rectangle"""
        if (self.__width == 0 or self.__height == 0):
            return (0)
        return (2 * (self.__width + self.__height))

    def __str__(self):
        if (self.__width == 0 or self.__height == 0):
            return ("")
        return ((str(self.print_symbol) * self.__width)
                + ("\n" + (str(self.print_symbol) * self.__width))
                * (self.__height - 1))

    def __repr__(self):
        return ("Rectangle({}, {})".format(self.__width, self.__height))

    def __del__(self):
        """Delete an instance of class Rectangle"""
        print("Bye rectangle...")
        type(self).number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if (type(rect_1) is not Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if (type(rect_2) is not Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if (rect_1.area() > rect_2.area()):
            return (rect_1)
        elif (rect_2.area() > rect_1.area()):
            return (rect_2)
        else:
            return (rect_1)

    @classmethod
    def square(cls, size=0):
        return (cls(size, size))
