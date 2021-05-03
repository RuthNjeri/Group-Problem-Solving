# Given an array of integers nums and an integer k, return the total number of continuous subarrays whose sum equals to k.


# Example 1:

# Input: nums = [1,1,1], k = 2
# Output: 2
# Example 2:

# Input: nums = [1,2,3], k = 3
# Output: 2

# Input: nums = [9, -9, 8, 1], k = 9
# Output: 3
from collections import defaultdict


class Solution:
    def subarraySum(self, nums, k):
        sums, count, current_sum = defaultdict(int), 0, 0

        sums[0] = 1

        for num in nums:
            current_sum += num

            if current_sum - k in sums:
                count += sums[current_sum - k]

            sums[current_sum] += 1

        return count


print(Solution().subarraySum([1, 2, 3], k=3))
print(Solution().subarraySum([9, -9, 8, 1], k=9))
