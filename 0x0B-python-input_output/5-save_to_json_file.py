#!/usr/bin/python3
"""
Creates a function that writes an object
to a text file using a JSON representation
"""


import json


def save_to_json_file(my_obj, filename):
    """
    Writes an object to a text file
    using a JSON representation

    Args:
        my_obj (object)
        filename : name of file
    """
    with open(filename, "a", encoding="utf-8") as f:
        json.dump(my_obj, f)
