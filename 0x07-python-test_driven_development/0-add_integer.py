#!/usr/bin/python3
"""
Defines a function that takes
in 2 integers and returns the sum

"""


def add_integer(a, b=98):
    """Adds a + b

    Args:
        a (int): first integer
        b (int): second integer

    Returns:
        a + b
    """
    if ((type(a) is not int) and (type(a) is not float)):
        raise TypeError("a must be an integer")
    if ((type(b) is not int) and (type(b) is not float)):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
