#!/usr/bin/python3
"""Module contains the matrix_divided function."""


def matrix_divided(matrix, div):
    """
    Divides all the elements of the matrix.

    Args:
        matrix (list of lists): A list of lists.
        div (int, float): number that divides the matrix elements.

    Raises:
        TypeError: if matrix isn't a list of lists of integers or floats.
        TypeError: if each list of the matrix isn't of the same size.
        TypeError: if div isn't a number.
        ZeroErrorDivision: if div is 0.

    Returns: A new matrix containing the quotients of original matrix.
    """

    if not all(isinstance(row, list) and all(isinstance(element, (int, float))
               for element in row) for row in matrix):
        raise TypeError("matrix must be a matrix(list of lists) of\
                        integers/floats")
    row_len = set(len(row) for row in matrix)
    if len(row_len) != 1:
        raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    result_matrix = [[round(element / div, 2) for element in row]\
                     for row in matrix]
    return result_matrix
