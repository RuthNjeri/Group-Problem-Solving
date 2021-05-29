"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""


class Node:
    def __init__(self, x: int, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: Node) -> Node:
        mapping = {}

        current = head

        while current:
            mapping[current] = Node(current.val)
            current = current.next

        current = head

        while current:
            mapping[current].next = mapping.get(current.next)
            mapping[current].random = mapping.get(current.random)
            current = current.next

        return mapping.get(head)
