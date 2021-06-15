# https://leetcode.com/problems/merge-two-sorted-lists

# Definition for singly-linked list.
# class ListNode
#     attr_accessor :val, :next
#     def initialize(val = 0, _next = nil)
#         @val = val
#         @next = _next
#     end
# end
# @param {ListNode} l1
# @param {ListNode} l2
# @return {ListNode}

def merge_two_lists(l1, l2)
    
  return l1 if l1.nil? && l2.nil?
  
  return l1 if l2.nil?
  return l2 if l1.nil?
  
  node_1 = l1
  node_2 = l2
  head = nil
  
  
  if l1.val > l2.val
        head = l2
        node_2 = l2.next
  else
        head = l1
        node_1 = l1.next
  end
 current = head
  
 while node_1 != nil && node_2 != nil
     if node_1.val > node_2.val
         current.next = node_2
         current = current.next
         node_2 = node_2.next
     else
         current.next = node_1
         current = current.next
         node_1 = node_1.next
     end
 end

while node_1 != nil
    current.next = node_1
    current = current.next
    node_1 = node_1.next
end

while node_2 != nil
    current.next = node_2
    current = current.next
    node_2 = node_2.next
end

head
 
end