# https://leetcode.com/problems/add-two-numbers-ii/


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        l1, l2 = self.reverse(l1), self.reverse(l2)

        carry = 0
        dummy = current = ListNode()
        while l1 and l2:
            carry, result = divmod(l1.val + l2.val + carry, 10)
            current.next = ListNode(result)
            l1, l2, current = l1.next, l2.next, current.next

        while l1:
            carry, result = divmod(l1.val + carry, 10)
            current.next = ListNode(result)
            l1, current = l1.next, current.next

        while l2:
            carry, result = divmod(l2.val + carry, 10)
            current.next = ListNode(result)
            l2, current = l2.next, current.next

        if carry > 0:
            current.next = ListNode(carry)

        return self.reverse(dummy.next)

    def reverse(self, linkedList: ListNode):
        prev, current = None, linkedList

        while current:
            nextNode = current.next
            current.next = prev
            prev = current
            current = nextNode

        return prev