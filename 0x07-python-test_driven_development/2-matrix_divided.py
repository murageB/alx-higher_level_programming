#!/usr/bin/python3
"""

Matrix Division module

"""
def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix
    
    Args:
        matrix (list): matrix to be divided
        div (int/float): number to divide matrix

    Raises:
        TypeError: if matrix is not a list of integers/floats or rows in matrix are not of the same size 
                   and if div is not integer/float
        ZeroDivisionError: if div is equal to 0
    
    Return:
        a new matrix
    """
    if not isinstance(div , (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if not isinstance(matrix[i][j], (int, float)):
                raise TypeError("matrix must be a matrix (list of lists)"
                                 "of integers/floats")
        for j in matrix:
            if len(j) != len(matrix[0]):
                raise TypeError("Each row of the matrix must have the same size")
    return [list(map(lambda x: round(x / div, 2), r))for r in matrix]
    
