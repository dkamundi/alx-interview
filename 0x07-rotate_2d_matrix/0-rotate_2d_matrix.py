#!/usr/bin/python3

def rotate_2d_matrix(matrix):
    """
    Rotate a 2D matrix 90 degrees clockwise in-place.

    Args:
    - matrix: A 2D matrix (list of lists).

    Returns:
    - None: The matrix is edited in-place.
    """
    matrix_len = len(matrix)

    for i in range(matrix_len // 2):
        for j in range(i, matrix_len - 1 - i):
            # Perform a four-way swap
            temp = matrix[i][j]
            matrix[i][j] = matrix[matrix_len - 1 - j][i]
            matrix[matrix_len - 1 - j][i] = matrix[matrix_len - 1 - i][matrix_len - 1 - j]
            matrix[matrix_len - 1 - i][matrix_len - 1 - j] = matrix[j][matrix_len - 1 - i]
            matrix[j][matrix_len - 1 - i] = temp
