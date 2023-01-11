#!/usr/bin/python3
"""
Creates a function that returns the dictionary
description with simple data for JSON
serialization of an object
"""


def class_to_json(obj):
    """
    Returns the dictionary description
    with simple data structure
    for JSON serialization of an object

    Args:
        obj : instance of a class
    """
    return (obj.__dict__)
