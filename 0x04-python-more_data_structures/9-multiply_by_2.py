#!/usr/bin/python3

def multiply_by_2(a_dictionary):
    if a_dictionary:
        new_dict = {}
        for keys in a_dictionary:
            new_dict[keys] = a_dictionary[keys] * 2
        return new_dict
    return a_dictionary
