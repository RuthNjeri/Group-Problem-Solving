# https://leetcode.com/problems/pacific-atlantic-water-flow/submissions/

class Solution:
  def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pacific_queue, atlantic_queue = deque(), deque()
        results = []

        rows = len(heights)
        cols = len(heights[0])

        # left
        for i in range(rows):
            pacific_queue.append((i, 0))
        # top
        for i in range(cols):
            pacific_queue.append((0, i))

        pacific_water_flows = self.bfs_pacific(pacific_queue, heights)

        # right
        for i in range(rows):
            atlantic_queue.append((i, cols - 1))

        # bottom
        for i in range(cols):
            atlantic_queue.append((rows - 1, i))

        atlantic_water_flows = self.bfs_atlantic(atlantic_queue, heights)

        for i in range(rows):
            for j in range(cols):
                if atlantic_water_flows[i][j] == 1 and pacific_water_flows[i][j] == 1:
                    results.append([i, j])

        return results

  def bfs_pacific(self, queue, heights):
      rows = len(heights)
      cols = len(heights[0])

      pacific_water_flows = [[0 for _ in range(cols)] for _ in range(rows)]

      while queue:
          current = queue.popleft()
          row, col = current[0], current[1]
          previous_height = heights[row][col]
          pacific_water_flows[row][col] = 1

          for x, y in ((1,0), (-1, 0), (0, 1), (0, -1)):
              next_row, next_col = row + x, col + y

              if next_row < 0 or next_row >= rows or next_col < 0 or next_col >= cols or pacific_water_flows[next_row][next_col] == 1:
                  continue
              current_height = heights[next_row][next_col]
              if current_height < previous_height:
                  continue
              queue.append((next_row, next_col))

      return pacific_water_flows

  def bfs_atlantic(self, queue, heights):
      rows = len(heights)
      cols = len(heights[0])
      atlantic_water_flows = [[0 for _ in range(cols)] for _ in range(rows)]

      while queue:
          current = queue.popleft()
          row, col = current[0], current[1]
          previous_height = heights[row][col]

          atlantic_water_flows[row][col] = 1

          for x, y in ((1,0), (-1, 0), (0, 1), (0, -1)):
              next_row, next_col = row + x, col + y

              if next_row < 0 or next_row >= rows or next_col < 0 or next_col >= cols or atlantic_water_flows[next_row][next_col] == 1:
                  continue

              current_height = heights[next_row][next_col]
              if current_height < previous_height:
                  continue

              queue.append((next_row, next_col))

      return atlantic_water_flows