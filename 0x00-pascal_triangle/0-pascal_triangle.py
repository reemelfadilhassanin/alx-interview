#!/usr/bin/python3
    """ this class defines the pascal traingle
    """

def pascal_triangle(n):
    if n <= 0:
        return []

    triangle = []
    
    for i in range(n):
        row = [1] * (i + 1)  # Start with all 1s
        
        # Update row values based on the previous row
        if i > 1:
            for j in range(1, i):
                row[j] = triangle[i-1][j-1] + triangle[i-1][j]
        
        triangle.append(row)
    
    return triangle
