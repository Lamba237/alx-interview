#!/usr/bin/python3
"""Pascal triangle"""


def pascal_triangle(n):
    """
    pascal_triangle: function that returns a pascal triangle

    Args:
        n: list
        Return: list of lists of containing the pascal triangle
    """

    if n <= 0:
        return []

    x = [[1]]
    # iterate over list from 1 to n-1
    for i in range(1, n):
        current_row = [1]
        for j in range(1, i):
            current_row.append(x[i-1][j-1] + x[i-1][j])
        current_row.append(1)
        x.append(current_row)

    return x
