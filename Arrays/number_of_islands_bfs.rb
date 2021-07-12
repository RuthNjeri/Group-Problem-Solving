# https://leetcode.com/problems/number-of-islands/
def num_islands(grid)
    count = 0

    for row in 0...grid.length
        for col in 0...grid[0].length
            if grid[row][col] == "1"
                count += 1
                bfs([[row, col]], grid)
            end
        end
    end
    count
end

def bfs(queue, grid)
    
    directions = [0, 1, 0, -1, 0]
    queued = Array.new(grid.length){Array.new(grid[0].length, false)}
    queued[queue[0][0]][queue[0][1]] = true
    
    
    while queue.length > 0
        cell = queue.shift
        row = cell[0]
        col = cell[1]
        # Sink the Island
        grid[row][col] = "0"
        
        # Traverse to the top, bottom, left, right..
        for index in 0...directions.length - 1
            next_row = row + directions[index]
            next_col = col + directions[index + 1]

            if next_row >= 0 && next_col >= 0 && next_row < grid.length && next_col < grid[0].length
                if grid[next_row][next_col] == "1" && !queued[next_row][next_col]
                    queue << [next_row, next_col]
                    queued[next_row][next_col] = true
                end
            end
        end
    end
end
