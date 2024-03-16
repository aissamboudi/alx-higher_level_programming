#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix:
        for arr in matrix:
            for item in arr:
                if item == arr[-1]:
                    print("{:d}".format(item), end="")
                else:
                    print("{:d}".format(item), end=" ")
            print('')
