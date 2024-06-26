#!/usr/bin/python3
"""function that divides all elements of a matrix."""
def matrix_divided(matrix, div):
    """divides all elements of a matrix."""
    if not all(isinstance(row, list) for row in matrix) or not all(isinstance(item, (int, float)) for row in matrix for item in row):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if len(set(len(row) for row in matrix)) > 1:
        raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    new_matrix = [[round(item / div, 2)
                   for item in row] for row in matrix]

    return new_matrix
