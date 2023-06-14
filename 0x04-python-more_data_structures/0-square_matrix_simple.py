#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    for row in matrix:
        lists = []
        for element in row:
            lists.append(element*element)
        new_matrix.append(lists)
    return new_matrix
