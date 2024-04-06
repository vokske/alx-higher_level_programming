#!/usr/bin/python3

def update_dictionary(a_dictionary, key, value):
    dict_1 = dict([key, value])
    a_dictionary.update(dict_1)
    print(a_dictionary)
