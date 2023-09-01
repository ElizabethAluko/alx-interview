#!/usr/bin/python3

import sys


def is_safe(board, row, col, N):
    """
    Check if it's safe to place a queen at a given position.

    Args:
        board (list[list[int]]): The current board configuration.
        row (int): The row to check.
        col (int): The column to check.
        N (int): The size of the board.

    Returns:
        bool: True if it's safe, False otherwise.
    """
    for i in range(col):
        if board[row][i] == 1:
            return False

    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    for i, j in zip(range(row, N, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True


def solve_nqueens_util(board, col, N):
    """
    Recursive utility function to solve the N queens problem.

    Args:
        board (list[list[int]]): The current board configuration.
        col (int): The current column.
        N (int): The size of the board.

    Returns:
        bool: True if a solution is found, False otherwise.
    """
    if col >= N:
        print_solution(board, N)
        return True

    res = False
    for i in range(N):
        if is_safe(board, i, col, N):
            board[i][col] = 1
            res = solve_nqueens_util(board, col + 1, N) or res
            board[i][col] = 0

    return res


def solve_nqueens(N):
    """
    Solve the N queens problem and print solutions.

    Args:
        N (int): The size of the board.
    """
    board = [[0 for _ in range(N)] for _ in range(N)]
    if not solve_nqueens_util(board, 0, N):
        print("No solution exists for N =", N)


def print_solution(board, N):
    """
    Print the board configuration for a solution.

    Args:
        board (list[list[int]]): The board configuration.
        N (int): The size of the board.
    """
    solution = []
    for i in range(N):
        for j in range(N):
            if board[i][j] == 1:
                solution.append([i, j])
    print(solution)


def main():
    """
    Main function to handle command-line arguments and solve N queens problem.
    """
    if len(sys.argv) == 1:
        print("Usage: 0-nqueens.py N")
        sys.exit(1)
    if len(sys.argv) != 2:
        print("Usage: ./0-nqueens.py N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    solve_nqueens(N)


if __name__ == "__main__":
    main()
