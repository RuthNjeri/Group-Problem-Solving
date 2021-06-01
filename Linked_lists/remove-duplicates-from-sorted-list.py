"""
https://leetcode.com/problems/remove-duplicates-from-sorted-list
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head:
            return head

        current = head
        node = head

        while current is not None:
            while node and node.val == current.val:
                node = node.next

            if not current.next:
                break

            current.next = node
            current = current.next

        return head
