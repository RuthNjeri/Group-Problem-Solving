# https://leetcode.com/problems/sum-root-to-leaf-numbers/
from typing import int

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        self.total = 0
        self.dfs(root, 0)
        return self.total

    def dfs(self, root, current_sum):
        if root is None:
            return
        current_sum = current_sum * 10 + root.val
        if root.left is None and root.right is None:
            self.total += current_sum
        self.dfs(root.left, current_sum)
        self.dfs(root.right, current_sum)
