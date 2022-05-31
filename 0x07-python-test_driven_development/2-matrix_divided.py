#!/usr/bin/python3
"""
1. Divide a matrix
"""


def matrix_divided(matrix, div):
    """
    function that divides all elements of a matrix
    """
    Typeerror1 = "matrix must be a matrix (list of lists) of integers/floats"
    Typeerror2 = "Each row of the matrix must have the same size"
    Typeerror3 = "div must be a number"
    Zeroerror = "division by zero"

    if not type(matrix) == list:
        raise TypeError(Typeerror1)
    if not type(div) == int and not type(div) == float:
        raise TypeError(Typeerror3)
    if div == 0:
        raise ZeroDivisionError(Zeroerror)
    if not matrix:
        raise TypeError(Typeerror1)
    if not type(matrix[0]) == list:
        raise TypeError(Typeerror1)
    new_matrix = []
    for i in matrix:
        if not type(i) == list:
            raise TypeError(Typeerror1)
        if not len(i) == len(matrix[0]):
            raise TypeError(Typeerror2)
        row = []
        for j in i:
            if not type(j) == int and not type(j) == float:
                raise TypeError(Typeerror1)
            row.append(round(j/div, 2))
        new_matrix.append(row)
    return new_matrix
