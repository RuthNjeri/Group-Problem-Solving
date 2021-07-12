# https://leetcode.com/problems/maximum-product-subarray/

from typing import int, List

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        current_max = current_min = best_max = nums[0]

        for num in nums[1:]:
            prev_min = min(current_min * num)
            current_min = min(prev_min, current_max * num, num)
            current_max = max(prev_min, current_max * num, num)
            best_max = max(current_max, best_max)

        return best_max