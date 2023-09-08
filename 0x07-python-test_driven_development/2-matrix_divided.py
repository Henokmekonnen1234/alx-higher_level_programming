#!/usr/bin/python3
"""
Module 2-matrix_divided.py

This module will show how to divide matrix
"""


def matrix_divided(matrix, div):
    """This function divide the  matrix values

    Args:
        matrix (list): lists of list of integer and float
        div (int, float): integer or float number

    Raise:
        TypeError: if matrix is not a matrix (list of lists) of integers/floats
        TypeError: Each row of the matrix does't have the same size
        TypeError: if div is not a number
        ZeroDivisionError: if div is zero

    Returns:
        list: returns result of the matrix divided by div
    """
    for i in range(len(matrix)):
        if i < len(matrix) - 1:
            if len(matrix[i]) != len(matrix[i + 1]):
                raise TypeError('Each row of the matrix must have'
                                ' the same size')
        for j in range(len(matrix[i])):
            if type(matrix[i][j]) != int and type(matrix[i][j]) != float:
                print("checked")
                raise TypeError('matrix must be a matrix (list of lists)'
                                ' of integers/floats')
    if type(div) not in (int, float):
        raise TypeError("div must be a number")
    elif div == 0:
        raise ZeroDivisionError("division by zero")
    i = list(map(lambda x: list(map(lambda y: round(y / div, 2), x)), matrix))
    return i
