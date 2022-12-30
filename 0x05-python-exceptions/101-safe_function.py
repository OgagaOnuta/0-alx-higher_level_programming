#!/usr/bin/python3

import sys


def safe_function(fct, *args):
    try:
        return (fct(*args))
    except Exception as escp:
        print("Exception: {}".format(escp), file=sys.stderr)
        return (None)
