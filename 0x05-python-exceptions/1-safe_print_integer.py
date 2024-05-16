#!/usr/bin/python3
def safe_print_integer(value):
    count = 0
    try:
        print("{:d}".format(value))
        return True
    except (TypeError, ValueError):
        return False
