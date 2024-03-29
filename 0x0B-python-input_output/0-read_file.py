#!/usr/bin/python3
"""Creates a function that reads a text file
(UTF8) and prints it to standard output
"""


def read_file(filename=""):
    """Reads a text file and prints it to stdout

    Args:
        filename : name of file

    """
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
