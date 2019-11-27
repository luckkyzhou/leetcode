from typing import List
class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        color = {}
        stack = []
        for i in range(len(graph)):
            if i not in color:
                stack.append(i)
                color[i] = 0
                while stack:
                    node = stack.pop()
                    for neighbor in graph[node]:
                        if neighbor not in color:
                            stack.append(neighbor)
                            color[neighbor] = color[node] ^ 1
                        elif color[neighbor] == color[node]:
                            return False
        return True