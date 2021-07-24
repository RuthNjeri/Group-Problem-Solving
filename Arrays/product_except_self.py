#https://leetcode.com/problems/product-of-array-except-self/description/

from typing import List, int

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        prefix = [0 for _ in range(length)]
        prefix[0] = 1
        postfix = [0 for _ in range(length)]
        postfix[length - 1] = 1

        for index in range(1, length):
            prefix[index] = prefix[index - 1] * nums[index - 1]

        for index in range(length - 2, -1, -1):
            postfix[index] = postfix[index + 1] * nums[index + 1]

        return [prefix[index] * postfix[index] for index in range(length)]
