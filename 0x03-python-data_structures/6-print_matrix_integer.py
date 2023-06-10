#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if len(matrix) == 0:
        return
    for row in matrix:
        for elemnt in row:
            print("{}".format(elemnt), end=' ')
        print()
