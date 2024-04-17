#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    i = 0
    print_list = []
    try:
        while i < x:
            print_list.append(my_list[i])
            i += 1
    except IndexError:
        print("That number exceeds the number of list elements")
    except:
        print("An unexpected error occured")
    else:
        for elements in print_list:
            print(elements, end="")
        print()
    return i
