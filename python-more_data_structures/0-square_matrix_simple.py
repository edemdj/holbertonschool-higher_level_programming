#!/usr/bin/python3
def square_matrix_simple(matrix=[]):

    if len(matrix) < 0:
        return []
    result = []
    for row in matrix:
        squared_row = []
        for num in row:
            squared_row.append(num ** 2)
        result.append(squared_row)
    return result
