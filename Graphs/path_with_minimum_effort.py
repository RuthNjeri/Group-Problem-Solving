# https://leetcode.com/problems/path-with-minimum-effort/
# Binary Search solution
class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        self.rows, self.cols = len(heights), len(heights[0])

        left, right = 0, 10000000

        while left < right:
            mid = left + (right - left) // 2

            if self.canReachDestination(mid, heights):
                right = mid
            else:
                left = mid + 1

        return left

    def is_valid(self, x, y):
        if x < 0 or x >= self.rows or y < 0 or y >= self.cols:
            return False
        return True

    def canReachDestination(self, mid, heights):
        visited = set()
        queue = deque()
        queue.append([0, 0])

        while queue:
            cell = queue.popleft()
            x, y = cell[0], cell[1]

            if x == self.rows - 1 and y == self.cols - 1:
                return True
            visited.add((x, y))

            for dx, dy in ((1, 0), (0, 1), (-1, 0), (0, -1)):
                adj_x, adj_y = x + dx, y + dy
                if self.is_valid(adj_x, adj_y) and (adj_x, adj_y) not in visited:
                    current_difference = abs(heights[adj_x][adj_y] - heights[x][y])

                    if current_difference <= mid:
                        visited.add((adj_x, adj_y))
                        queue.append([adj_x, adj_y])

        return False

# Bruteforce Solution

class Solution_2:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        self.row = len(heights)
        self.col = len(heights[0])
        self.directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        self.max_so_far = float('inf')
        self.heights = heights
        return self.dfs(0, 0, 0)

    def is_valid(self, x, y):
        if x < 0 or x >= self.row or y < 0 or y >= self.col:
            return False
        return True

    def dfs(self, x, y, max_difference):
        if x == self.row - 1 and y == self.col - 1:
            self.max_so_far = min(self.max_so_far, max_difference)
            return max_difference

        current_height = self.heights[x][y]
        self.heights[x][y] = 0
        min_effort = float('inf')

        for dx, dy in self.directions:
            adj_x = x + dx
            adj_y = y + dy

            if self.is_valid(adj_x, adj_y) and self.heights[adj_x][adj_y] != 0:
                current_difference = abs(self.heights[adj_x][adj_y] - current_height)
                max_current_difference = max(max_difference, current_difference)
                if max_current_difference < self.max_so_far:
                    result = self.dfs(adj_x, adj_y, max_current_difference)
                    min_effort = min(min_effort, result)
        self.heights[x][y] = current_height
        return min_effort