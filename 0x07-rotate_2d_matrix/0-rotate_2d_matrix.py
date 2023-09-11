#!/usr/bin/python3
"""Contains a function that rotate n × n 2D matrix by 90 degrees clockwise"""


def rotate_2d_matrix(matrix):
    """Rotate non-empty 2 dimensuons matrix by 90 degrees
    clockwisely in place.

     Return:
        Nothing.
    """
    n = len(matrix)
    matrix_tmp = []

    for j in range(n):
        matrix_tmp_item = []
        for i in range(-1, -n-1, -1):
            matrix_tmp_item.append(matrix[i][j])
        matrix_tmp.append(matrix_tmp_item)
    for i in range(n):
        matrix[i] = matrix_tmp[i]
