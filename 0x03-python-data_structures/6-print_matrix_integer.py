#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix is None:
        return
    for row in matrix:
        for elemnt in row:
            print("{}".format(elemnt), end=' ')
        print()
