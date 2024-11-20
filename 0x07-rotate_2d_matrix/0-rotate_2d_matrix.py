#!/usr/bin/python3
"""
Rotate 2D Matrix by 90 clockwise.
"""

def rotate_2d_matrix(matrix):
    """
    Rotates an n x n 2D matrix 90clockwise.
    
    The matrix is modified in place.
    
    Args:
        matrix (list of list of ints): The 2D to rotate.
    """
    # Step 1: Transpose the matrix
    n = len(matrix)
    for i in range(n):
        for j in range(i, n):
            # Swap elements (i, j) with (j, i)
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    for i in range(n):
        matrix[i].reverse()

