"""
https://leetcode.com/problems/count-servers-that-communicate
"""
from typing import List


class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        comp_total = 0

        # Account for the server count in rows
        for row in grid:
            comp_total = (comp_total + sum(row)) if sum(row) > 1 else comp_total

        # Account for the server count in columns
        for j in range(len(grid[0])):
            col_total = self.get_col_sum(grid, j)
            comp_total = (comp_total + col_total) if col_total > 1 else comp_total

        # Remove duplicates that were counted in the row and column count
        duplicates = 0
        row_count = 0
        for row in grid:
            for column in range(len(row)):
                if sum(row) > 1 and self.get_col_sum(grid, column) > 1 and grid[row_count][column] == 1:
                    duplicates = duplicates + 1
            row_count = row_count + 1

        comp_total = comp_total - duplicates
        return comp_total

    def get_col_sum(self, grid, column):
        """
        Gets the number of servers communicating within a column.

        :param grid:
        :param column:
        :return:
        """
        total = 0
        for k in range(len(grid)):
            total = total + grid[k][column]

        return total
