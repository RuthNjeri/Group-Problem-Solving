# https://leetcode.com/problems/search-in-a-sorted-array-of-unknown-size/

# """
# This is ArrayReader's API interface.
# You should not implement it, or speculate about its implementation
# """
#class ArrayReader:
#    def get(self, index: int) -> int:

class Solution:
    def search(self, reader, target):
        if target == reader.get(0):
            return 0

        left, right = 0, 1

        while target > reader.get(right):
            left = right
            right *= 2
        
        while left <= right:
            mid = left + (right - left) // 2
            number = reader.get(mid)

            if number > target:
                right = mid - 1
            elif number < target:
                left = mid + 1
            else:
                return mid
        return -1
