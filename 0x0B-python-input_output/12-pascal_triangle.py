#!/usr/bin/python3
"""12. Pascal's Triangle"""


def pascal_triangle(n):
    """returns a list of lists of integers
    representing the Pascal’s triangle of n"""
    if n <= 0:
        return []

    pascal_trian = [[1]]

    for i in range(1, n):
        row = [1]
        for p in range(1, i):
            row.append(pascal_trian[i-1][p-1] + pascal_trian[i-1][p])
        row.append(1)
        pascal_trian.append(row)
    return pascal_trian
