#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    if matrix is not None:
        matrix2 = matrix.copy()
        matrix2 = list(map(lambda i: i * i, matrix2))
        return matrix2
