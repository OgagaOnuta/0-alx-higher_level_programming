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

try:
    listed = loaded(filed) + sys.argv[1:]
except Exception:
    with open(filed, "w", encoding="utf-8") as f:
        for i in sys.argv[1:]:
            listed = f.write(i)
finally:
    saved(listed, filed)
