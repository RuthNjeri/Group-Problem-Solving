###################
# Leetcode 117. Populating Next Right Pointers in Each Node II
# https://leetcode.com/problems/populating-next-right-pointers-in-each-node-ii/
####################

"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

# This implementation uses extra space

from collections import deque


class Solution:
    def connect(self, root):
        if root is None:
            return root

        queue = deque()
        queue.append([root])

        while len(queue) > 0:
            nodes = queue.popleft()

            new_nodes = []
            for index, node in enumerate(nodes):
                # Point to the next node in the level
                if index < len(nodes) - 1:
                    node.next = nodes[index + 1]

                if node.left:
                    new_nodes.append(node.left)

                if node.right:
                    new_nodes.append(node.right)
            # check if anything was added to new_nodes[] before adding to the queue
            if len(new_nodes) > 0:
                queue.append(new_nodes)

        return root
