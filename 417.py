from typing import List

class Solution:
    def pacificAtlantic(self, matrix: List[List[int]]) -> List[List[int]]:
        m = len(matrix)
        if m == 0: return []
        n = len(matrix[0])
        Pacific = [[False for _ in range(n)] for _ in range(m)]
        Atlantic = [[False for _ in range(n)] for _ in range(m)]
        res = []

        for i in range(m):
            self.DFS(matrix, i, 0, Pacific, matrix[i][0])
            self.DFS(matrix, i, n - 1, Atlantic, matrix[i][n - 1])
        for j in range(n):
            self.DFS(matrix, 0, j, Pacific, matrix[0][j])
            self.DFS(matrix, m - 1, j, Atlantic, matrix[m - 1][j])

        for i in range(m):
            for j in range(n):
                if Pacific[i][j] and Atlantic[i][j]:
                    res.append([i, j])
        return res

    def DFS(self, matrix, i, j, visited, pre):
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        # 从边界开始找，找比自身大的
        if i < 0 or j < 0 or i >= len(matrix) or j >= len(matrix[0]) or visited[i][j] or matrix[i][j] < pre:
            return
        visited[i][j] = True
        for direction in directions:
            self.DFS(matrix, i + direction[0], j + direction[1], visited, matrix[i][j])