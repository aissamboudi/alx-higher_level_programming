#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary:
        maxval = max(a_dictionary.values(), default=None)
        if maxval is not None:
            return next(key for key, value in a_dictionary.items() if value == maxval)
    else:
        return None
