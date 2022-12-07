#!/usr/bin/python3

def best_score(a_dictionary):
    if not isinstance(a_dictionary, dict):
        return None
    x = 0
    for key in a_dictionary:
        if a_dictionary[key] > x:
            ret = key
    return (key)
