#!/usr/bin/python3
"""Module contains the pascal_triangle function."""


def pascal_triangle(n):
    """
    Computes the Pascal's triangle of order n.
    
    Args:
        n: Order of the Pascal's triangle.

    Returns (list): A list of lists of integers representing the\
            Pascal's triangle.
    """
    triangle = []

    if n <= 0:
        return []
    for i in range(n):
        row = [1] * (i + 1)
        for j in range(1, i):
            row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
        triangle.append(row)
    for row in triangle:
        print(row)
    return triangle
