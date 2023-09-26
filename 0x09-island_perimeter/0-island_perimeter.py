#!/usr/bin/python3
"""Island Perimeter Module"""


def island_perimeter(grid):
    """Calculate the perimeter of an island.

    args:
        grid: A list of list of integers.

    Returns:
        Perimeter of the island defined by the grid.
    """
    if not grid:
        return 0

    perimeter = 0
    rows, columns = len(grid), len(grid[0])

    for row in range(rows):
        for column in range(columns):
            if grid[row][column] == 1:
                perimeter += 4

                # check adjacent cells (up, down, left and right)
                if row > 0 and grid[row - 1][column] == 1:
                    perimeter -= 2
                if column > 0 and grid[row][column - 1] == 1:
                    perimeter -= 2
    return perimeter
