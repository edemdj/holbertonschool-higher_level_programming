#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for x in matrix:
        for i in range(len(x)):
            print("{}".format(x[i]), end="")
            if i != len(x) - 1:
                print(" ", end="")
        print("")
