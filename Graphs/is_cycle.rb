# You are given a directed graph consisting of N vertices, numbered from 1 to N, and N edges.

# The graph is described by two arrays, A and B, both of length N. A pair A[K], B[K] (for K from 0 to N-1)
# describes a directed edge from vertex A[K] to vertex B[K].
# Note that the graph might contain self-loops (edges where A[K] = B[K]) and/or multiple edges between the same pair of vertices.

# Your task is to check whether the given graph is a cycle. A graph is a cycle if it is possible to start at some vertex and,
# by following the provided edges, visit all the other vertices and return to the starting point.

# For example, A = [1, 3, 2, 4] and B = [4, 1, 3, 2] is a cycle of length 4.
# On the other hand, A = [1, 2, 3, 4] and B = [2, 1, 4, 3] is not a cycle. The graph consist of two disjoint cycles of length 2 each.
# Given A = [1, 2, 1] and B = [2, 3, 3], your function should return false.
# Given A = [1, 2, 3, 4] and B = [2, 1, 4, 4], your function should return false.
# Given A = [1, 2, 3, 4] and B = [2, 1, 4, 3], your function should return false.
# Given A = [1, 2, 2, 3, 3] and B = [2, 3, 3, 4, 5], your function should return false.

require 'pry'
def is_cycle(a, b)
  visited = {}
  adj_list = {}
  start_node = 1
  stack = [1]
  visited_nodes = 0

  for node in 0...a.length
    if adj_list[a[node]].nil?
      adj_list[a[node]] = [b[node]]
    else
      return false if adj_list[a[node]] # If a node has more than one neighbor, that means the graph is not a cycle
    end
  end

  while !stack.empty?
    current_node = stack.pop
    break if visited[current_node]
    visited[current_node] = true
    visited_nodes += 1
    if !adj_list[current_node].nil?
      stack << adj_list[current_node][0]
    end
  end

  current_node == start_node && visited_nodes == a.length ? true : false

end

# p is_cycle([1, 2, 1], [3, 2, 2]) #false
p is_cycle([1, 2, 2, 3, 3] ,[2, 3, 3, 4, 5]) #false
# Check the above if a node is not present in A then it is not a cycle
# p is_cycle([1, 2, 3, 4], [2, 1, 4, 4]) #false
# p is_cycle([1, 2, 1], [2, 3, 3]) #false
p is_cycle([3, 1, 2], [2, 3, 1]) #true
# p is_cycle([3, 1, 2], [2, 3, 1]) #true
# p is_cycle([1, 2, 3, 4], [2, 1, 4, 4]) #false
# p is_cycle([1, 2, 3, 4], [2, 1, 4, 3]) #false
# p is_cycle([1, 2], [1, 2]) #false
p is_cycle([1, 3, 2, 4], [4, 1, 3, 2]) #true
# p is_cycle([5, 3, 1, 2, 4], [4, 5, 5, 1, 2]) #false