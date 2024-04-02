#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    sq_matrix = list(map(lambda row: list(map(lambda i: i**2, row)), matrix))
    return sq_matrix
