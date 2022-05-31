#!/usr/bin/python3
"""
1. Divide a matrix
"""


def matrix_divided(matrix, div):
    """
    function that divides all elements of a matrix
    """
    if not type(matrix) == list:
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if not type(div) == int and not type(div) == float:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if not matrix:
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if not type(matrix[0]) == list:
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    new_matrix = []
    for i in matrix:
        if not type(i) == list:
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
        if not len(i) == len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")
        row = []
        for j in i:
            if not type(j) == int and not type(j) == float:
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
            row.append(round(j/div, 2))
        new_matrix.append(row)
    return new_matrix
