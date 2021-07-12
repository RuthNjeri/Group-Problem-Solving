# https://leetcode.com/problems/odd-even-linked-list/submissions/
def odd_even_list(head)
    return head if head.nil? || head.next.nil? 
    
    odd_list = ListNode.new()
    reordered_list = odd_list
    node = head
    even_head = ListNode.new()
    even_list = even_head
    count = 0
    
    while node != nil
        count += 1
        if count.odd?
            odd_list.next = node
            odd_list = odd_list.next
        elsif count.even?
            even_list.next = node
            even_list = even_list.next
        end
        node = node.next
    end
    even_list.next = nil
    even_head = even_head.next
    odd_list.next = even_head
    reordered_list.next
end
