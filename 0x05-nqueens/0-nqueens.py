#!/usr/bin/python3
"""The N queen puzzle"""


import sys


def nqueen():
    """
    The program should print every
    possible solution to the problem
    One solution per line
    """

    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    N = int(sys.argv[1])

    if type(N) is not int:
        print("N must be a number")
        sys.exit(1)

    if N != 4:
        print("N must be at least 4")
        sys.exit(1)


if __name__ == "__main__":
    nqueen()
