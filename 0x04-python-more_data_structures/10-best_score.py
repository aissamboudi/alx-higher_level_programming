#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary == None:
        return None
    Mval = [key for key, value in a_dictionary.items() if value == max(a_dictionary.values())]
    if len(Mval) > 0:
        return Mval[0]
    else:
        return None
