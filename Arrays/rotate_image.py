# https://leetcode.com/problems/rotate-image/

from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        size, layers = len(matrix) - 1, len(matrix) // 2

        for layer in range(layers):
            for i in range(layer, size - layer):
                top = (matrix[layer][0],)
                right = matrix[i][size - layer]
                bottom = matrix[size - layer][size - i]
                left = matrix[size - i][layer]

                matrix[layer][i] = left
                matrix[i][size - layer] = top
                matrix[size - layer][size - i] = right
                matrix[size - i][layer] = bottom
        return matrix