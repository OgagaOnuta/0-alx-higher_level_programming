#!/usr/bin/python3
"""
Adds all arguments to a Python list,
and saves them to a file
"""


import sys
loaded = __import__('6-load_from_json_file').load_from_json_file
saved = __import__('5-save_to_json_file').save_to_json_file

filed = "add_item.json"
listed = []
listed = listed + sys.argv[1:]

saved(listed, filed)
listed = loaded(filed)
