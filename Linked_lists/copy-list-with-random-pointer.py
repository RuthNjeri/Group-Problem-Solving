"""
https://leetcode.com/problems/copy-list-with-random-pointer/

This question was brought to class on May 24th.

"""


# Definition for a Node.
class Node:
    def __init__(self, x: int, next: "Node" = None, random: "Node" = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    """
    This solution is accepted by LeetCode.
    """

    def copyRandomList(self, head: "Node") -> "Node":
        if not head:
            return head

        random_index_tracker = []  # This is used to keep track of the index of node.random in the original list
        if not head.random:
            random_index_tracker.append(None)
        else:
            random_index_tracker.append(self.get_position(head, head.random))

        head2 = Node(head.val)
        current2 = head2

        current = head.next

        # Create the deep copy, populating only the node.val and node.next, but not node.random.
        # For each node in the original list, keep a track of the index where its node.random is pointing.
        while current:

            if not current.random:
                random_index_tracker.append(None)
            else:
                random_index_tracker.append(self.get_position(head, current.random))

            node = Node(current.val)
            current2.next = node

            current, current2 = current.next, current2.next

        # Go ahead to populate the node.random for all nodes in the deep copy
        current2 = head2

        for j in range(len(random_index_tracker)):
            if random_index_tracker[j] is None:
                current2 = current2.next
                continue

            random_pointer = head2
            for k in range(random_index_tracker[j]):
                random_pointer = random_pointer.next

            current2.random = random_pointer
            current2 = current2.next

        return head2

    def get_position(self, head: "Node", node: "Node"):
        """
        Given a node, find out how far it is from the head. This is similar to finding the index of an item in a list.

        :param head:
        :param node:
        :return:
        """
        index = 0
        current = head

        while current != node:
            index = index + 1
            current = current.next

        return index


# Alternative Soltion.
class Solution2:
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
