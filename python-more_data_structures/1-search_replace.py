#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = my_list[:]
    for i, search in enumerate(my_list):
            if search == 2:
                new_list[i] = replace
    return new_list
