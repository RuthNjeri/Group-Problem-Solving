"""
https://leetcode.com/problems/trapping-rain-water
"""
from typing import List


class Solution1:
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


class Solution2:
    def trap(self, height: List[int]) -> int:
        # This is a O(N^2) solution
        water = 0
        for i in range(1, len(height)):
            max_left, max_right = max(height[:i]), max(height[i:])
            current = min(max_left, max_right) - height[i]
            if current > 0:
                water += current
        return water


class Solution2:
    def trap(self, height: List[int]) -> int:
        # This is a DP solution with a Time Complexity of O(N) solution
        # It is similar to Solution1 but makes use of prefilled arrays
        water = 0
        size = len(height)

        if len(height) == 0:
            return water

        max_left, max_right = [0 for _ in range(size)], [0 for _ in range(size)]
        max_left[0], max_right[size - 1] = height[0], height[size - 1]

        for i in range(1, size):
            max_left[i] = max(max_left[i - 1], height[i])

        for i in range(size - 2, -1, -1):
            max_right[i] = max(max_right[i + 1], height[i])

        for i in range(size):
            current = min(max_left[i], max_right[i]) - height[i]
            if current > 0:
                water += current
        return water