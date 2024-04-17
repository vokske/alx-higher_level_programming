#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    count = 0
    try:
        for element in range(x):
            print(element, end="")
            count += 1
    except IndexError:
        break
    print()
    return count
