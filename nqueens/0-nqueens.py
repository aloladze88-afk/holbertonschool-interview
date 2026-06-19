#!/usr/bin/python3
"""Solve the N Queens puzzle."""

import sys


def is_safe(queens, row, col):
    """Check if a queen can be safely placed at [row, col]."""
    for queen_row, queen_col in queens:
        if queen_col == col:
            return False

        if abs(queen_row - row) == abs(queen_col - col):
            return False

    return True


def solve_nqueens(n, row, queens):
    """Place queens row by row using backtracking."""
    if row == n:
        print(queens)
        return

    for col in range(n):
        if is_safe(queens, row, col):
            queens.append([row, col])
            solve_nqueens(n, row + 1, queens)
            queens.pop()


if len(sys.argv) != 2:
    print("Usage: nqueens N")
    sys.exit(1)

try:
    n = int(sys.argv[1])
except ValueError:
    print("N must be a number")
    sys.exit(1)

if n < 4:
    print("N must be at least 4")
    sys.exit(1)

solve_nqueens(n, 0, [])
