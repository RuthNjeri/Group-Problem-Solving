#
# https://leetcode.com/problems/add-two-numbers/
# Reversed lists


# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        carry = 0
        dummy = current = ListNode()

        while l1 and l2:
            carry, result = divmod(l1.val + l2.val + carry, 10)
            current.next = ListNode(result)
            current = current.next
            l1, l2 = l1.next, l2.next

        while l1:
            carry, result = divmod(l1.val + carry, 10)
            current.next = ListNode(result)
            current = current.next
            l1 = l1.next

        while l2:
            carry, result = divmod(l2.val + carry, 10)
            current.next = ListNode(result)
            current = current.next
            l2 = l2.next

        if carry > 0:
            current.next = ListNode(carry)

        return dummy.next
