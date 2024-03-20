#!/usr/bin/python3
def search_replace(my_list, search, replace):
    cplist = my_list.copy()
    for i in range(len(cplist)):
        if cplist[i] == search:
            cplist[i] = replace
    return cplist
