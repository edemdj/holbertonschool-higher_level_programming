#!/usr/bin/python3
def print_list_integer(my_list=[]):
    for list in my_list:
        if list < 0:
            return
        else:
            print("{:d} ".format(list))
