#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix:
        for arr in matrix:
            for item in arr:
                print(item,end=" ")
            print('')
