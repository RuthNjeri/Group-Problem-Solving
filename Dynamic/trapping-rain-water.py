"""
https://leetcode.com/problems/trapping-rain-water
"""
from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) < 1:
            return 0

        max_left = []  # Defines the maximum height of an element to the left of an index
        max_left.append(height[0])

        for j in range(1, len(height)):
            max_left.append(max(height[j], max_left[j - 1]))

        max_right = []  # Defines the maximum height of an element to the right of an index
        max_right.append(height[len(height) - 1])

        for j in range(len(height) - 2, -1, -1):
            max_right.append(max(height[j], max_right[len(height) - j - 2]))
        max_right.reverse()

        total_water = 0
        for j in range(len(height)):
            min_height = min(max_left[j], max_right[j])
            water_height = min_height - height[j]
            total_water = total_water + water_height if water_height > 0 else total_water

        return total_water
