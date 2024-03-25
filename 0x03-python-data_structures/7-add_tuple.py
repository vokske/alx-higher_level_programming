#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    if len(tuple_a) < 2:
        list_a = list(tuple_a)
        while len(list_a) < 2:
            list_a.append(0)
    if len(tuple_b) < 2:
        list_b = list(tuple_b)
        while len(list_b) < 2:
            list_b.append(0)
    sum_list = [list_a[0] + list_b [0], list_a[1] + list_b[1]]
    return tuple(sum_list)
