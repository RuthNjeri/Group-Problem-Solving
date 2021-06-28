# @param {Integer[][]} heights
# @return {Integer}
# https://leetcode.com/problems/path-with-minimum-effort/

# Optimum solution...but still getting a timeout error on Leetcode...maybe it is the language?

def minimum_effort_path(heights)
  rows = heights.length
  cols = heights[0].length

  min_effort = Array.new(heights.length){Array.new(heights[0].length, Float::INFINITY)}
  min_effort[0][0] = 0

  queued = Array.new(heights.length){Array.new(heights[0].length, false)}
  queue = [[0,0]]

  queued[0][0] = true

  while queue.length > 0
      cell = queue.shift
      next_node = [0, 1, 0, -1, 0]
      row = cell[0]
      col = cell[1]
      queued[row][col] = false

      for index in 0...next_node.length - 1
          next_row = row + next_node[index]

          next_col = col + next_node[index + 1]

          if next_row >= 0 && next_col >= 0 && next_row < rows  && next_col < cols

              effort = [min_effort[row][col], (heights[row][col] - heights[next_row][next_col]).abs].max

              if effort < min_effort[next_row][next_col]
                  min_effort[next_row][next_col] = effort
                  if !queued[next_row][next_col]
                      queue.unshift([next_row, next_col])
                      queued[next_row][next_col] = true
                  end
              end
          end
      end
  end

  min_effort[rows - 1][cols - 1]
end






# Bruteforce solution
def minimum_effort_path_bruteforce(heights)
  return 0 if heights.length == 1 && heights[0].length == 1

  visited = Array.new(heights.length) {Array.new(heights[0].length, 0)}
  max_effort(0, 0, heights, visited, -Float::INFINITY)
end

def max_effort(row, col, heights, visited, effort)
 return effort if row == heights.length - 1 && col == heights[0].length - 1

 visited[row][col] = 1
 current_cell = heights[row][col]

 up, down, left, right = Float::INFINITY, Float::INFINITY, Float::INFINITY, Float::INFINITY

 up   =  max_effort(row - 1, col, heights,
         visited,[effort, (current_cell - heights[row - 1][col]).abs].max ) if row - 1 >= 0 && visited[row - 1][col] != 1

 down =  max_effort(row + 1, col, heights,
         visited, [effort, (current_cell - heights[row + 1][col]).abs].max) if row + 1 < heights.length && visited[row + 1][col] != 1

 left =  max_effort(row, col - 1, heights,
         visited, [effort, (current_cell - heights[row][col - 1]).abs].max ) if col - 1 >= 0 && visited[row][col - 1] != 1

 right =  max_effort(row, col + 1, heights,
          visited, [effort, (current_cell - heights[row][col + 1]).abs].max) if col + 1 < heights[0].length && visited[row][col + 1] != 1

visited[row][col] = 0
[up, down, left, right].min
end

# tests
# [[1,10,6,7,9,10,4,9]]
# [[3]]
# [[1,2,2],[3,8,2],[5,3,5]]
# [[1,2,3],[3,8,4],[5,3,5]]
# [[1,2,1,1,1],[1,2,1,2,1],[1,2,1,2,1],[1,2,1,2,1],[1,1,1,2,1]]


# Time Limit exceeded
# [[4,3,4,10,5,5,9,2],[10,8,2,10,9,7,5,6],[5,8,10,10,10,7,4,2],[5,1,3,1,1,3,1,9],[6,4,10,6,10,9,4,6]]