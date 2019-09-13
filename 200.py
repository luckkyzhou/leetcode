# -*- coding: utf-8 -*-

from typing import List

class Solution:
    directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]

    def DFS(self, grid, i, j, m, n, marked):
        marked[i][j] = True
        for direction in self.directions:
            new_i = i + direction[0]
            new_j = j + direction[1]
            if 0 <= new_i < m and 0 <= new_j < n and not marked[new_j][new_j] and grid[new_i][new_j] == '1':
                self.DFS(grid, new_i, new_j, m, n, marked)