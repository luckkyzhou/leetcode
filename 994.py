from typing import List
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = []
        time = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2: queue.append((i, j, time))

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        while queue:
            i, j, time = queue.pop(0)
            for direction in directions:
                new_i = i + direction[0]
                new_j = j + direction[1]
                if 0 <= new_i < len(grid) and 0 <= new_j < len(grid[0]) and grid[new_i][new_j] == 1:
                    grid[new_i][new_j] = 2
                    queue.append((new_i, new_j, time + 1))

        for i in range(len(grid)):
            if 1 in grid[i]: return -1
        return time