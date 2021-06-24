"""
https://leetcode.com/problems/find-all-anagrams-in-a-string

This was brought up in class on 12th June as one of the CodeHunt questions.
"""

from typing import List


class Solution:
    """
    This is accepted by LeetCode.
    """

    def findAnagrams(self, s: str, p: str) -> List[int]:
        results = []
        sorted_p = sorted(p)

        for j in range(len(s) - len(p) + 1):
            substr = s[j:j + len(p)]

            if sorted(substr) == sorted_p:
                results.append(j)

        return results
