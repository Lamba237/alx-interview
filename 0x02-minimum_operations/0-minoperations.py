#!/usr/bin/python3
"""
 Minimum Operations
"""

def minOperations(n):
    """
    minOperations: a method that
    calculates the fewest number of operations
    needed to resultin exactly n H characters in the file.

    Args:
      n: a number
      Return: an integer number
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