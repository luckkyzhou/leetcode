# -*- coding: utf-8 -*-

from typing import List

class Solution:
    directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]

    # m是行数，n是列数
    # 深度搜索函数
    def DFS(self, grid, i, j, m, n, marked):
        marked[i][j] = True
        for direction in self.directions:
            new_i = i + direction[0]
            new_j = j + direction[1]
            # 如果坐标不越界，没被搜索过，此时为陆地，则继续搜索算法
            if 0 <= new_i < m and 0 <= new_j < n and not marked[new_i][new_j] and grid[new_i][new_j] == '1':
                self.DFS(grid, new_i, new_j, m, n, marked)

    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        marked = [[False for x in range(n)] for x in range(m)]
        count = 0

        for i in range(m):
            for j in range(n):
                if not marked[i][j] and grid[i][j] == '1':
                    self.DFS(grid, i, j, m, n, marked)
                    count += 1
        return count

if __name__ == '__main__':
    solution = Solution()
    grid = [['1', '1', '1', '1', '0'],
            ['1', '1', '0', '1', '0'],
            ['1', '1', '0', '0', '0'],
            ['0', '0', '0', '0', '0']]
    result = solution.numIslands(grid)
    print(result)


