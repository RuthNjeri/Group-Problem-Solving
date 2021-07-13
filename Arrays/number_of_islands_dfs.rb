# https://leetcode.com/problems/number-of-islands/

def num_islands(grid)
    count = 0 # 0
    
    rows = grid.length - 1 # 3
    cols = grid[0].length - 1 # 4
    
    for row in 0..rows # 0..3 # m * n
        for col in 0..cols # 0..4
            if grid[row][col] == "1" # 0,0
                dfs(row, col, grid)
                count += 1 # 1, 2, 3
            end
        end
    end
    count 
end

def dfs(row, col, grid) # 0, 0; grid, out of bounds; 1, 0, grid; 1, 1, grid; 0, 1, grid  m * n
    # base case
    return if row < 0 || col < 0 || row >= grid.length || col >= grid[0].length
    return if grid[row][col] == "0"
    
   # process it
    grid[row][col] = "0"
    
   # call the top, bottom, left, right
    dfs(row - 1, col, grid) # top # returns
    dfs(row + 1, col, grid) # bottom
    dfs(row, col - 1, grid) # left
    dfs(row, col + 1, grid) # right
end
