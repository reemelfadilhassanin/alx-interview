#!/usr/bin/python3
"""Defines island perimeter finding function."""

def island_perimeter(grid):
    """Return the perimeter of an island in a grid.
    
    The grid represents water by 0 and land by 1. For each land cell,
    we count its exposed edges (edges adjacent to water or the grid boundary).
    
    Args:
        grid (list of list of int): A 2D grid where 1 represents land
                                    and 0 represents water.
                                    
    Returns:
        int: The perimeter of the island defined by land cells (1s) in the grid.
        
    The perimeter is calculated by:
        - Counting all edges of land cells (each land cell contributes 4 edges).
        - Subtracting edges shared with adjacent land cells (each shared edge reduces perimeter by 2).
    
    Example:
        grid = [
            [0, 0, 0, 0, 0, 0],
            [0, 1, 0, 0, 0, 0],
            [0, 1, 0, 0, 0, 0],
            [0, 1, 1, 1, 0, 0],
            [0, 0, 0, 0, 0, 0]
        ]
        >>> island_perimeter(grid)
        12
    """
    width = len(grid[0])
    height = len(grid)
    edges = 0
    size = 0

    for i in range(height):
        for j in range(width):
            if grid[i][j] == 1:
                size += 1
                if (j > 0 and grid[i][j - 1] == 1):  # Left neighbor is land
                    edges += 1
                if (i > 0 and grid[i - 1][j] == 1):  # Top neighbor is land
                    edges += 1

    # Perimeter calculation
    return size * 4 - edges * 2
