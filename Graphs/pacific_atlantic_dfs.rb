# https://leetcode.com/problems/pacific-atlantic-water-flow/

def pacific_atlantic(heights)
  return [] if heights.empty?
  pacific = Array.new(heights.length) { Array.new(heights[0].length, false) }
  atlantic = Array.new(heights.length) { Array.new(heights[0].length, false) }

  # left side pacific column
  for i in 0...heights.length
    dfs(heights, i, 0, pacific)
  end

  # upper side pacific row
  for j in 0...heights[0].length
    dfs(heights, 0, j, pacific)
  end

  # right side atlantic column
  for i in 0...heights.length
    dfs(heights, i, heights[0].length - 1, atlantic)
  end

  # down side atlantic row
  for j in 0...heights[0].length
    dfs(heights, heights.length - 1, j, atlantic)
  end
  res = []
  for i in 0...heights.length
    for j in 0...heights[0].length
      res << [i, j] if pacific[i][j] && atlantic[i][j]
    end
  end
  res
end

def dfs(heights, i, j, visited)
  visited[i][j] = true
  dfs(heights, i+1, j, visited) if i+1 < heights.size && !visited[i+1][j] && heights[i+1][j] >= heights[i][j]
  dfs(heights, i-1, j, visited) if i-1 >= 0 && !visited[i-1][j] && heights[i-1][j] >= heights[i][j]
  dfs(heights, i, j+1, visited) if j+1 < heights[0].size && !visited[i][j+1] && heights[i][j+1] >= heights[i][j]
  dfs(heights, i, j-1, visited) if j-1 >= 0 && !visited[i][j-1] && heights[i][j-1] >= heights[i][j]
end



