#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    list = [set_1, set_2]
    result = set()
    for i in list:
        result =result.symmetric_difference(i)
    return result
