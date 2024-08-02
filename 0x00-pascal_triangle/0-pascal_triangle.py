#!/usr/bin/python3
"""Pascal triangle"""


def pascal_triangle(n):
    """This function returns a list o lists of
    integers representing a pascal triangle
    Args:
        n: list of list
        Return: List of integers
    """

    if n <= 0:
        return []

    triangle = [[1]]  # Initializing first row

    for i in range(1, n):
        prev_row = triangle[-1]
        new_row = [1]
        for j in range(1, i):
            new_row.append(prev_row[j - 1] + prev_row[j])
        new_row.append(1)
        triangle.append(new_row)

    return triangle
