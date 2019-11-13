from typing import List

class Solution:
    def minCostII(self, costs: List[List[int]]) -> int:
        if costs == []: return 0
        for i in range(1, len(costs)):
            for j in range(len(costs[0])):
                # min中用+号
                costs[i][j] += min(costs[i - 1][:j] + costs[i - 1][j + 1:])
        return min(costs[-1])