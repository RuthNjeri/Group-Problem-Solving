# Definition for a binary tree node.
# class TreeNode
#     attr_accessor :val, :left, :right
#     def initialize(val = 0, left = nil, right = nil)
#         @val = val
#         @left = left
#         @right = right
#     end
# end
# @param {TreeNode} root
# @param {Integer} k
# @return {Integer}

def kth_smallest(root, k)
  # Inorder traversal?
  @elements = []
  inorder(root)
  @elements[k - 1]
end

def inorder(root)
  return if root == nil
  
  inorder(root.left)
  @elements << root.val
  inorder(root.right)
end



# Alternative

def kth_smallest(root, k)
  # Inorder traversal?
  @k = k
  @element = nil
  inorder(root, 0)
  @element
end

def inorder(root, k)
  return k + 1 if root == nil
  
  position = inorder(root.left, k)
  @element = root.val if position == @k
  inorder(root.right, position) # 2, 1
end