#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        row_output = " ".join(map(str, row))
        print("{}".format(row_output))
