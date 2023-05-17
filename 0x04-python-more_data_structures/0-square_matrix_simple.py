#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    x = matrix.copy()

    for z in range(len(matrix)):
        x[z] = list(map(lambda y: y**2, matrix[z]))

    return (x)
