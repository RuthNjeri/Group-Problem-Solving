def eventual_safe_nodes(graph)
  visited = Array.new(graph.length, 0) #[1,1,2,1,0,2,0]
  results = []
  counter = 0

  for node in 0...graph.length # 0
      dfs(node, graph, visited)
  end

  while counter < visited.length
      results << counter if visited[counter] == 2
      counter += 1
  end
  results
end

def dfs(node, graph, visited)
 return visited[node] if visited[node] == 1 || visited[node] == 2

  visited[node] = 1
  result = 2 if graph[node].length == 0

  for neighbor in graph[node]
     result =  dfs(neighbor, graph, visited)
     break if result == 1
  end

  visited[node] =  result
  visited[node]
end