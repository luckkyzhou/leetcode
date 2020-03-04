from typing import List
class Solution:
    def gardenNoAdj(self, N: int, paths: List[List[int]]) -> List[int]:
        from collections import defaultdict
        graph = defaultdict(list)
        for i, j in paths:
            graph[i - 1].append(j - 1)
            graph[j - 1].append(i - 1)

        res = [0 for _ in range(N)]
        for node in range(N):
            res[node] = ({1,2,3,4} - {res[neighbor] for neighbor in graph[node]}).pop()
        return res