#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    keys = set(a_dictionary.keys())
    key = list(keys & {key})
    if len(key) > 0:
        a_dictionary.pop(key[0])
    return a_dictionary
