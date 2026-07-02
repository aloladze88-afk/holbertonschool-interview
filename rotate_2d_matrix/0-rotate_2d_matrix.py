#!/usr/bin/python3
"""Rotate a 2D matrix."""


def rotate_2d_matrix(matrix):
    """Rotate an n x n 2D matrix 90 degrees clockwise in-place."""
    n = len(matrix)

    for row in range(n):
        for col in range(row, n):
            matrix[row][col], matrix[col][row] = matrix[col][row], matrix[row][col]

    for row in matrix:
        row.reverse()
