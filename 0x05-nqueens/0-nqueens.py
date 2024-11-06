#!/usr/bin/python3
import sys

def is_safe(board, row, col, N):
    """Check if it's safe to place a queen at board[row][col]."""
    # Check column
    for i in range(row):
        if board[i][col] == 1:
            return False

    # Check upper-left diagonal
    for i, j in zip(range(row-1, -1, -1), range(col-1, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check upper-right diagonal
    for i, j in zip(range(row-1, -1, -1), range(col+1, N)):
        if board[i][j] == 1:
            return False

    return True

def solve_nqueens(board, row, N, solutions):
    """Backtracking to solve the N Queens problem."""
    if row == N:
        solution = []
        for r in range(N):
            for c in range(N):
                if board[r][c] == 1:
                    solution.append([r, c])
        solutions.append(solution)
        return
    
    for col in range(N):
        if is_safe(board, row, col, N):
            board[row][col] = 1
            solve_nqueens(board, row + 1, N, solutions)
            board[row][col] = 0  # backtrack

def main():
    """Main function to handle input and output."""
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = [[0 for _ in range(N)] for _ in range(N)]  # initialize the board with 0s
    solutions = []
    solve_nqueens(board, 0, N, solutions)

    for solution in solutions:
        print(solution)

if __name__ == "__main__":
    main()
