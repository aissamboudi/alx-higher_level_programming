#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    dp = sorted(a_dictionary.items())
    for key, value in dp:
        print("{}: {}".format(key, value))
