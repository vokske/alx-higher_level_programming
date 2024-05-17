#!/usr/bin/python3

import sys

def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
        return True
    except Exception as te:
        print(f"Exception: {te}", file=sys.stderr)
        return False


value = "sempe"
result = safe_print_integer_err(value)
print(result)
