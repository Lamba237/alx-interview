#!/usr/bin/python3
"""Function returns minimum number of operations to get n"""


def minOperations(n):
    """This function returns the minimum
    number of operations to get n
    Args:
        n: int
    Returns: returns an integer
    """

    if n <= 1:
        return 0

    operations = 0
    factor = 2

    while n > 1:
        while n % factor == 0:
            operations += factor
            n //= factor
        factor += 1

    return operations
