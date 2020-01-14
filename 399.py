from typing import List
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = {}

        for (x, y), z in zip(equations, values):
            if x in graph: graph[x][y] = z
            else: graph[x] = {y : z}
            if y in graph: graph[y][x] = 1 / z
            else: graph[y] = {x : 1/z}

        def dfs(s, t) -> int:
            if s not in graph: return -1
            if t == s: return 1

            for node in graph[s].keys():
                if node == t: return graph[s][node]
                elif node not in visited:
                    visited.add(node)
                    z = dfs(node, t)
                    if z != -1: return graph[s][node] * z
            return -1

        res = []
        for s,t in queries:
            visited = set()
            res.append(dfs(s,t))
        return res