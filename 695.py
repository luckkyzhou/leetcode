from typing import List

class Solution:
    def __init__(self):
        self.count = 0
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        res = []
        m = len(grid)
        n = len(grid[0])
        visited = [[False for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 and not visited[i][j]:
                    self.count = 0
                    self.DFS(grid, i, j, visited)
                    res.append(self.count)
        if res == []: return 0
        return max(res)

    def DFS(self, matrix, i, j, visited):
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        m = len(matrix)
        n = len(matrix[0])
        visited[i][j] = True
        if matrix[i][j] == 1:
            self.count += 1
        for direction in directions:
            new_i = i + direction[0]
            new_j = j + direction[1]
            if 0 <= new_i < m and 0 <= new_j < n and not visited[new_i][new_j] and matrix[new_i][new_j] == 1:
                self.DFS(matrix, new_i, new_j, visited)


if __name__ == '__main__':
    solution = Solution()
    res = solution.maxAreaOfIsland([[1,1],[1,0]])
    print(res)