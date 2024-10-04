#!/usr/bin/python3
"""
This module defines the function to generate Pascal's Triangle.
"""

from typing import List

def pascal_triangle(n: int) -> List[List[int]]:
	"""
	Returns a list of lists of integers representing
	the Pascal’s triangle of n.
	
	If n <= 0, return an empty list.
	"""
	if n <= 0:
		return []

	triangle = [[1]]  # Start with the first row

	for i in range(1, n):
		row = [1]  # Each row starts with a 1
		for j in range(len(triangle[i - 1]) - 1):
			# Sum the two values from the previous row
			row.append(triangle[i - 1][j] + triangle[i - 1][j + 1])
		row.append(1)  # Each row ends with a 1
		triangle.append(row)  # Append the constructed row to the triangle

	return triangle
