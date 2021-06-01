# https://leetcode.com/problems/unique-paths/
# O(m * n) ST
def unique_paths(m, n)
  grid = Array.new(m){Array.new(n - 1)}

  # The paths on the top row are 1s
  # The cells on the right are 1s
  # For optimization, this can be done inside the double
  # for loop..if col == 0 the cell is 1, and or if row == 0 the cell is 1
  for col in 0...n
      grid[0][col] = 1
  end

  for row in 1...m
      for col in 0...n
          up = row - 1
          left = col - 1
          if grid[up][col] != nil && grid[row][left] != nil
              grid[row][col] = grid[up][col] + grid[row][left]
          else
              grid[row][col] = grid[up][col] if grid[up][col] != nil
              grid[row][col] = grid[row][left]if grid[row][left] != nil
          end
      end
  end
  grid[m - 1][n - 1]
end