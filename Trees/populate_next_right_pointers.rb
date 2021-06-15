# Definition for a Node.
# class Node
#     attr_accessor :val, :left, :right, :next
#     def initialize(val)
#         @val = val
#         @left, @right, @next = nil, nil, nil
#     end
# end

# @param {Node} root
# @return {Node}

# https://leetcode.com/problems/populating-next-right-pointers-in-each-node-ii/submissions/

# Solution 1
def connect(root)
    
  return root if root == nil
  
  queue = [root, nil]
  
  while queue.length > 0
      node = queue.shift
      return root if node == nil && queue.length == 0
      if node == nil
          queue << nil
          next
      end
      node.next = queue.first
      queue << node.left if node.left
      queue << node.right if node.right
  end
  root
end

# Solution 2
def connect(root)
  return root if root.nil?
  
  queue = [root]
  
  while queue.length > 0
      level = []
      for position in 0...queue.length
          node = queue[position]
          node.next = queue[position + 1]
          
          level << node.left if node.left
          level << node.right if node.right
      end
      queue = level
  end
  root
end