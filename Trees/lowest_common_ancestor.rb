# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/

# Definition for a binary tree node.
# class TreeNode
#     attr_accessor :val, :left, :right
#     def initialize(val)
#         @val = val
#         @left, @right = nil, nil
#     end
# end

# @param {TreeNode} root
# @param {TreeNode} p
# @param {TreeNode} q
# @return {TreeNode}

def lowest_common_ancestor(root, p, q)
  @ancestor = root
  
  dfs_helper(root, p, q)

  @ancestor
  
end

def dfs_helper(root, p, q)
  
  return if root.right
  here, left, right = false, false, false
  if root.val == p.val || root.val == q.val
      here = true
  end
      

  left = dfs_helper(root.left, p, q) if root.left != nil
  right = dfs_helper(root.right, p, q) if root.right != nil
  

  if here && left || here && right || left && right
      @ancestor = root
  end

  here || left || right
end