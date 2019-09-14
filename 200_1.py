# -*- coding: utf-8 -*-

from typing import List
from collections import deque

class Solution():
    directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]

    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        if m == 0:
            return 0
        n = len(grid[0])
        marked = [[False for x in range(n)] for x in range(m)]
        count = 0

        for i in range(m):
            for j in range(n):
                # 坐标没被标记过，且其值为1
                if not marked[i][j] and grid[i][j] == '1':
                    # 定义队列
                    queue = deque()
                    queue.append((i, j))
                    marked[i][j] = True
                    # 队列中有坐标时
                    while queue:
                        # 队首出坐标
                        cur_x, cur_y = queue.popleft()
                        for direction in self.directions:
                            new_x = cur_x + direction[0]
                            new_y = cur_y + direction[1]
                            if 0 <= new_x < m and 0 <= new_y < n and not marked[new_x][new_y] and grid[new_x][new_y] == '1':
                                # 队尾加入0-3个坐标
                                queue.append((new_x, new_y))
                                marked[new_x][new_y] = True
                    count += 1
        return count

if __name__ == '__main__':
    grid = [['1', '1', '1', '1', '0'],
            ['1', '1', '0', '1', '0'],
            ['1', '1', '0', '0', '0'],
            ['0', '0', '0', '0', '0']]
    solution = Solution()
    result = solution.numIslands(grid)
    print(result)
