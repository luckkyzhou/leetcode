from typing import List

class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:
        visited = [False for _ in range(len(M))]
        res = 0
        for i in range(len(M)):
            if not visited[i]:
                self.DFS(M, visited, i)
                res += 1
        return res

    def DFS(self, matrix, visited, i):
        for j in range(len(matrix)):
            if matrix[i][j] == 1 and not visited[j]:
                visited[j] = True
                self.DFS(matrix, visited, j)