#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if len(matrix) == 0 or all(len(row) == 0 for row in matrix) :
        print()
    for row in matrix:
        count = 0
        for elemnt in row:
            if count == len(row) - 1:
                print("{:d}".format(elemnt))
            else:
                print("{:d}".format(elemnt), end=' ')
            count +=1
