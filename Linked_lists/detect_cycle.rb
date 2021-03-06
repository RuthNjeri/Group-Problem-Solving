# Two pointer problem.
# Have a fast and slow moving pointer in the Linked List
# The fast pointer moves twice as fast
# If the slow pointer moves one step, the fast pointer moves two steps
# They will eventually meet if it is a cycle

def hasCycle(head) # O(n)T, O(1)S
  fast, slow = head, head

  while fast != nil && fast.next != nil
      slow = slow.next
      fast = fast.next.next
      return true if slow == fast
  end
  false
end