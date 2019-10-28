from typing import List

class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        m = len(maze)
        n = len(maze[0])
        visited = [[False for _ in range(n)] for _ in range(m)]

        def DFS(i, j):
            if i == destination[0] and j == destination[1]:
                return True
            visited[i][j] = True

            for direction in directions:
                new_i = i
                new_j = j
                while 0 <= new_i + direction[0] < m and 0 <= new_j + direction[1] < n and maze[new_i + direction[0]][new_j + direction[1]] == 0:
                    new_i += direction[0]
                    new_j += direction[1]
                if new_i == i and new_j == j: continue
                if visited[new_i][new_j] == False:
                    if DFS(new_i, new_j):
                        return True
            return False

        return DFS(start[0], start[1])