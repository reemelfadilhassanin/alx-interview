#!/usr/bin/python3
"""
This module defines the function to generate Pascal's Triangle.
"""

def pascal_triangle(n):
    """
    Returns a list of lists of integers representing
    the Pascal’s triangle of n.
    """
    tra = []
    if n <= 0:
        return tra
    
    tra = [[1]]
    for i in range(1, n):
        temp = [1]  # Start each row with a 1
        for j in range(len(tra[i - 1]) - 1):
            curr = tra[i - 1]
            temp.append(curr[j] + curr[j + 1])  # Calculate the inner values
        temp.append(1)  # End each row with a 1
        tra.append(temp)
    
    return tra
