#!/usr/bin/python3
"""
 Rotate 2D Matrix.
"""


def rotate_2d_matrix(matrix):
    """
    Given an n x n 2D matrix, rotate it 90 degrees clockwise.
    """
    n = len(matrix)
    for layer in range(n // 2):
        first, last, offset = layer, n - 1 - layer, 0
        for j in range(first, last):
            top = matrix[first][j]
            matrix[first][j] = matrix[last - offset][first]
            matrix[last - offset][first] = matrix[last][last - offset]
            matrix[last][last - offset] = matrix[j][last]
            matrix[j][last] = top
            offset += 1
