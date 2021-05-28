"""
https://leetcode.com/problems/valid-sudoku/

This was presented to class on May 24th.

Initialize an empty hash
For every row:
if (the cell is a number) and (the number does not exist in the hash) and (the number lies between 1 and 9):
    add it to the hash
else
    return false -> because this number is repeated in that row

Repeat these steps for every column

Repeat these steps for every 3 x 3 grid
"""


from typing import List
from collections import defaultdict


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        # -------------------------------
        # This deals with all my rows
        # -------------------------------
        for j in range(9):
            row_num_hash = {}

            for k in range(9):

                if board[j][k] != '.':

                    if board[j][k] not in row_num_hash and 0 < int(board[j][k]) < 10:
                        row_num_hash[board[j][k]] = 'exists'
                    else:
                        return False

        # -------------------------------
        # This deals with all my columns
        # -------------------------------
        for j in range(9):
            col_num_hash = {}

            for k in range(9):

                if board[k][j] != '.':

                    if board[k][j] not in col_num_hash and 0 < int(board[k][j]) < 10:
                        col_num_hash[board[k][j]] = 'exists'
                    else:
                        return False

        # -------------------------------
        # This deals with all my grids
        # -------------------------------
        grid_num_hash = defaultdict(
            lambda: set())  # The key will be a grid coordinate, e.g. "0-1" for the grid on row 0, column1
        # The value will be a set which holds the numbers for that grid

        separator = '-'
        for j in range(9):
            for k in range(9):

                if board[j][k] != '.':

                    if board[j][k] in grid_num_hash[separator.join((str(int(j / 3)), str(int(k / 3))))]:
                        return False
                    else:
                        grid_num_hash[separator.join((str(int(j / 3)), str(int(k / 3))))].add(board[j][k])

        return True
