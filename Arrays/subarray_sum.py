# Given an array of integers nums and an integer k, return the total number of continuous subarrays whose sum equals to k.


# Example 1:

# Input: nums = [1,1,1], k = 2
# Output: 2
# Example 2:

# Input: nums = [1,2,3], k = 3
# Output: 2

# Input: nums = [9, -9, 8, 1], k = 9
# Output: 3

# In this solution, keep a count of the prefix sum you have seen in a hash
# if prefix_sum - k exists in the hash, increment the count with the hash[prefix_sum - k]

from collections import defaultdict # O(n)ST


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

# Without extra memory(Bruteforce)
# Use a double for loop each time resetting the sum to 0 in the outer for loop
# add the values in the inner for loop and increment the count if the sum == k
# The code below is in Ruby, it has a timeout on Leetcode but the Java implementation passes

def subarray_sum(nums, k) # O(1)S, O(n^2)T
    count = 0

    for start in 0...nums.length
        sum = 0
        for stop in start...nums.length
            sum += nums[stop]
            count += 1 if sum == k
        end
    end
    count
end

print(Solution().subarraySum([1, 2, 3], k=3))
print(Solution().subarraySum([9, -9, 8, 1], k=9))
