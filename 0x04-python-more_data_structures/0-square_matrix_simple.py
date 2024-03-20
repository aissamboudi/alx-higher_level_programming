#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    nmatrix = [row[:] for row in matrix]
    for i in range(len(nmatrix)):
        for j in range(len(nmatrix[i])):
            nmatrix[i][j] = nmatrix[i][j]*nmatrix[i][j]
    return nmatrix
