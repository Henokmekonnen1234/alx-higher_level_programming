#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    if matrix is not None:
        matrix2 = matrix.copy()
        matrix2 = [[row[i] * row[i] for row in matrix2] for i in range(3)]
        return matrix2
