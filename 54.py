# -*- coding: utf-8 -*-
from typing import List

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res, i, j, di, dj = [], 0, 0, 0, 1

        if matrix != []:
            m, n = len(matrix), len(matrix[0])
            for x in range(m * n):
                res.append(matrix[i][j])
                # 走过的地方标记为0
                matrix[i][j] = 0
                # 判断是否转弯，对i+di%长度非常精妙
                if matrix[(i + di) % m][(j + dj) % n] == 0:
                    di, dj = dj, -di
                # 变换旋转方向
                i += di
                j += dj
        return res