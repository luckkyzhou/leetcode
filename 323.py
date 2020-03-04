from typing import List
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        from collections import defaultdict
        graph = defaultdict(list)
        visited = set()

        for edge in edges:
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])

        def DFS(node):
            visited.add(node)
            for neighbor in graph[node]:
                if neighbor not in visited:
                    DFS(neighbor)

        res = 0
        for i in range(n):
            if i not in visited:
                res += 1
                DFS(i)
        return res