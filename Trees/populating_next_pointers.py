# https://leetcode.com/problems/populating-next-right-pointers-in-each-node/
from collections import deque


class Node:
    def __init__(self, val: int = 0, left: "Node" = None, right: "Node" = None, next: "Node" = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: Node) -> Node:
        if root is None:
            return

        queue = deque([root])

        while queue:
            size = len(queue)

            for i in range(size):
                current = queue.popleft()
                if i < size - 1:
                    current.next = queue[0]
                if current.left:
                    queue.append(current.left)
                if current.right:
                    queue.append(current.right)
        return root
