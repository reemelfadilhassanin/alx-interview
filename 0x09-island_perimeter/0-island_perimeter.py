#!/usr/bin/python3

def island_perimeter(grid):
    """
    Returns the perimeter of the island in the grid.

    Args:
        grid: A list of list of integers representing the grid where 1 is land and 0 is water.

    Returns:
        The perimeter of the island.
    """
    perimeter = 0
    rows = len(grid)
    cols = len(grid[0])
    
    for i in range(rows):
        for j in range(cols):
            # If the current cell is land
            if grid[i][j] == 1:
                # Check the four neighbors (left, right, up, down)
                if i == 0 or grid[i - 1][j] == 0:  # Up
                    perimeter += 1
                if i == rows - 1 or grid[i + 1][j] == 0:  # Down
                    perimeter += 1
                if j == 0 or grid[i][j - 1] == 0:  # Left
                    perimeter += 1
                if j == cols - 1 or grid[i][j + 1] == 0:  # Right
                    perimeter += 1

    return perimeter
