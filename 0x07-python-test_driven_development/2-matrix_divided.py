#!/usr/bin/python3


'''
    2-matrix_divided.py

    Contains function that divides all elements of a matrix
'''


def matrix_divided(matrix, div):
    '''
    Python Function that divide a matrix by variable div
    '''

    listError = 'matrix must be a matrix (list of lists) of integers/floats'
    if type(matrix) is not list:
        raise TypeError(listError)
    for row in matrix:
        if type(row) is not list:
            raise TypeError(listError)

    for row in matrix:
        if len(matrix[0]) != len(row):
            raise TypeError("Each row of the matrix must have the same size")

    for row in matrix:
        for elem in row:
            if not isinstance(elem, (int, float)):
                raise TypeError(listError)
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    new = []
    for row in matrix:
        rows = []
        for elem in row:
            rows.append(round((elem/div), 2))
        new.append(rows)
    return new
