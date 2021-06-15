# https://leetcode.com/problems/kth-smallest-element-in-a-bst

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        self.k = k
        self.result = 0
        self.helper(root)
        return self.result

    def helper(self, root):
        if root is None:
            return
        self.helper(root.left)
        self.k -= 1
        if self.k == 0:
            self.result = root.val
        self.helper(root.right)