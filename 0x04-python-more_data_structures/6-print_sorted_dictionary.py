#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    dp = sorted(a_dictionary.items())
    for i in dp:
        print("{}: {}".format(i[0], dp[1]))
