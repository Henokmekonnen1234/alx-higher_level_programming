#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    if matrix is not None:
        matrix2 = matrix.copy()
        matrix2 = [i**2 for i in matrix2]
        return matrix2
