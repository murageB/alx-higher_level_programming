#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    for i in range(len(matrix)):
        new_matrix.append(list(map((lambda j: j ** 2), matrix[i])))
    return (new_matrix)
