# Definition for Node.
# class Node
#     attr_accessor :val, :next, :random
#     def initialize(val = 0)
#         @val = val
#		  @next = nil
#		  @random = nil
#     end
# end

# @param {Node} node
# @return {Node}


def copyRandomList(head)
  return head if head == nil
  
  nodes = {}

  new_head = Node.new(head.val)

  nodes[head] = new_head # old_7: new_7

  new_node = new_head
  node = head.next

  while node != nil
   new_node.next = Node.new(node.val) # 7 -> 13, 13 -> 11, 11 -> 10, 1.1

   nodes[node] = new_node.next # {13: 7.next}

   new_node = new_node.next # 7.next..13, 13.next..11, 11.next..10, 1
   node = node.next # 11, 10, 1, nil
  end

  rand_nodes = head # 7
  new_rand_nodes = new_head # 7

  while rand_nodes != nil
     if rand_nodes.random != nil
      new_rand_nodes.random = nodes[rand_nodes.random]
     end

     new_rand_nodes = new_rand_nodes.next # 13
     rand_nodes = rand_nodes.next # 13
  end

  new_head
end

