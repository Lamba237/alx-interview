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

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    def solve(n, row, queens, solutions):
        if row == n:
            solutions.append(queens.copy())
            return
        for col in range(n):
            if all(q_col != col and abs(q_row - row) != abs(q_col - col)
                    for q_row, q_col in enumerate(queens)):
                queens.append(col)
                solve(n, row + 1, queens, solutions)
                queens.pop()
    solutions = []
    solve(N, 0, [], solutions)
    for sol in solutions:
        print([[i, sol[i]] for i in range(N)])


if __name__ == "__main__":
    nqueen()
