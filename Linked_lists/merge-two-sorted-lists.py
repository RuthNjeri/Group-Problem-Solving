"""
https://leetcode.com/problems/merge-two-sorted-lists
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1 and not l2:
            return None

        if not l1:
            return l2

        if not l2:
            return l1

        current = l1 if l1.val < l2.val else l2
        head = current

        head1, head2 = l1, l2
        if head1 == current:
            head1 = head1.next
        else:
            head2 = head2.next

        # Go through the case when both head1 and head2 have items
        while head1 and head2:
            if head1.val < head2.val:
                current.next = head1
                current = current.next
                head1 = head1.next
            else:
                current.next = head2
                current = current.next
                head2 = head2.next

        # A number of items remain in the first list. Append them to the merge list
        if head1:
            while head1:
                current.next = head1
                head1, current = head1.next, current.next

        # A number of items remain in the second list. Append them to the merge list
        if head2:
            while head2:
                current.next = head2
                head2, current = head2.next, current.next

        return head
