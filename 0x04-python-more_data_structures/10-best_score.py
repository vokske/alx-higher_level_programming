#!/usr/bin/python3

def best_score(a_dictionary):
    if a_dictionary:
        max_score = 0
        for keys in a_dictionary:
            if a_dictionary[keys] > max_score:
                max_score = a_dictionary[keys]
        return max_score
    return None
