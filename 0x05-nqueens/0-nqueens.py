#!/usr/bin/python3
""" Solve the N Queens problem """
import sys

if len(sys.argv) != 2:
    print("Usage: nqueens N")
    exit(1)

try:
    n = int(sys.argv[1])
    if n < 4:
        print('N must be at least 4')
        exit(1)
except ValueError:
    print('N must be a number')
    exit(1)

def queens_position(n, row=0, col=[], diag1=[], diag2=[]):
    """
    Generate possible safe positions for the queen to be placed.

    Args:
        n: size of the chessboard
        row: The current row being considered for queen placement.
        col: A list that holds the column positions of queens for each row.
        diag1: List that holds the diagonal positions where queens are placed.
        diag2: List that holds the anti-diagonal positions where queens are placed.
    """
    if row < n:
        for j in range(n):
            if j not in col and row + j not in diag1 and row - j not in diag2:
                yield from queens_position(n, row + 1, col + [j], diag1 + [row + j], diag2 + [row - j])
    else:
        yield col

def solve_queens(n):
    """
    Iterate through the queens_position function and print the positions of queens for each solution generated.

    Args:
        n: size of the chessboard
    """
    solution_positions = []
    row_index = 0
    for solution in queens_position(n, 0):
        for col_index in solution:
            solution_positions.append([row_index, col_index])
            row_index += 1
        print(solution_positions)
        solution_positions = []
        row_index = 0

solve_queens(n)