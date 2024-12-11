#!/usr/bin/python3
""" Find the island perimeter """


def island_perimeter(grid):
    """
    returns the perimeter of the island described in grid
    where:
          grid is a list of list of integers:
              0 represents water
              1 represents land
              Each cell is square, with a side length of 1
              Cells are connected horizontally/vertically (not diagonally).
              grid is rectangular, with its width and height not exceeding 100

    Args:
        grid: list of list of integers
    
    Return: perimeter
    """
    perimeter = 0
    rows = len(grid)
    cols = len(grid[0])

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                # Check all four directions
                if i == 0 or grid[i-1][j] == 0:  # Up
                    perimeter += 1
                if i == rows-1 or grid[i+1][j] == 0:  # Down
                    perimeter += 1
                if j == 0 or grid[i][j-1] == 0:  # Left
                    perimeter += 1
                if j == cols-1 or grid[i][j+1] == 0:  # Right
                    perimeter += 1

    return perimeter