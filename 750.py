from typing import List
class Solution:
    def countCornerRectangles(self, grid: List[List[int]]) -> int:
        row = len(grid)
        col = len(grid[0])
        res = 0

        for i in range(row - 1):
            ones = set()
            for k in range(col):
                if grid[i][k] == 1: ones.add(k)
            for j in range(i + 1, row):
                tmp = 0
                for t in ones:
                    if grid[j][t] == 1: tmp += 1
                res += tmp * (tmp - 1) // 2
        return res