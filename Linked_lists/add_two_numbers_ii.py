"""
https://leetcode.com/problems/add-two-numbers-ii/
"""


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


class Solution:
    """
    This is an alternative solution that is accepted by LeetCode.
    """

    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        num1, num2 = self.list_to_str(l1), self.list_to_str(l2)

        sum = int(num1) + int(num2)
        sum_list = list(str(sum))

        head = ListNode(int(sum_list[0]))
        current = head

        for j in range(1, len(sum_list)):
            node = ListNode(int(sum_list[j]))
            current.next = node
            current = node

        return head

    def list_to_str(self, mylist: ListNode) -> str:
        number = ""
        node = mylist

        while node:
            number = number + str(node.val)
            node = node.next

        return number
