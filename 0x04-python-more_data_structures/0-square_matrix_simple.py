#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    for row in matrix:
        l = []
        for element in row:
            l.append(element*element)
        new_matrix.append(l)
    return new_matrix
