#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if len(matrix) == 0:
        return
    for row in matrix:
        count = 0
        for elemnt in row:
            count +=1
            if count == len(row) - 1
                print("{}".format(elemnt))
            else:
                print("{}".format(elemnt), end=' ')
        print()
