# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(self, root: "TreeNode", p: "TreeNode", q: "TreeNode") -> "TreeNode":
        return self.lcaHelper(root, p, q)

    def lcaHelper(self, root, p, q):
        if root is None:
            return False
        if root is q or root is p:
            return root
        left = self.lcaHelper(root.left, p, q)
        right = self.lcaHelper(root.right, p, q)

        if left is None and right is None:
            return False

        if left and right:
            return root

        return left if left else right
