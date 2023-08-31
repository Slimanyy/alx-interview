#!/usr/bin/env python3
"""N queens puzzle solution"""

import sys

def is_safe(board, row, col):
    """Check if it's safe to place a queen at board[row][col]"""
    for prev_row in range(row):
        if board[prev_row] == col or \
           board[prev_row] - prev_row == col - row or \
           board[prev_row] + prev_row == col + row:
            return False
    return True

def solve_nqueens(n, row=0, board=[]):
    """Recursively solve the N queens puzzle"""
    if row == n:
        print([[r, c] for r, c in enumerate(board)])
        return
    for col in range(n):
        if is_safe(board, row, col):
            board.append(col)
            solve_nqueens(n, row + 1, board)
            board.pop()

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

solve_nqueens(N)
