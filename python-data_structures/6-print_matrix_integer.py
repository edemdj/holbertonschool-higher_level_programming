#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for i in matrix:
        i_output = " ".join(map(str, i))
        print("{}".format(i_output))
