#!/usr/bin/python3
"""Module contains a script.
It adds all arguments to a Python list, and then savse them to a file.
"""

import json
import sys
import os

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

if os.path.exists("add_item.json"):
    my_list = load_from_json_file("add_item.json")
else:
    my_list = []
if len(sys.argv) > 1:
    for argument in sys.argv[1:]:
        my_list.append(argument)

save_to_json_file(my_file, "add_item.json")
