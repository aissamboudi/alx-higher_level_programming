#!/user/bin/python3
def print_sorted_dictionary(a_dictionary):
    dp = sorted(a_dictionary.keys())
    for i in dp:
        print("{}: {}".format(i, a_dictionary[i]))
