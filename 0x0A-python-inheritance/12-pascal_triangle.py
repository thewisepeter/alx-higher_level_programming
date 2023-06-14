#!/usr/bin/python3
"""module that returns a list of integers representing Pascals triangle"""


def pascal_triangle(n):
    """returns a list of lists of integers
        representing the Pascal’s triangle"""

    result = []
    for i in range(n):
        row = []
        for j in range(i + 1):
            if j == 0 or j == i:
                row.append(1)
            row.append(result[i - 1][j - 1] + result[i - 1][j])
        result.append(row)
    return result
