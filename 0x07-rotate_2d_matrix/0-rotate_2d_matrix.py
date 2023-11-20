#!/usr/bin/python3
"""
Rotates a 2D array by 90 degrees clockwise
"""


def rotate_2d_matrix(matrix):
    """
    Rotate a 2D matrix 90 degrees clockwise in-place.

    Args:
    - matrix: A 2D matrix (list of lists).

    Returns:
    - None: The matrix is edited in-place.
    """
    matrix_len = len(matrix)
    matrix_copy = [[x for x in row] for row in matrix]

    for i in range(0, matrix_len):
        for j in range(0, matrix_len):
            matrix[j][matrix_len - 1 - i] = matrix_copy[i][j]
