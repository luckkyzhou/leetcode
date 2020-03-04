from typing import List
class DSU:
    def __init__(self, N):
        self.pre = [i for i in range(N)]

    def find(self, root):
        if self.pre[root] != root:
            self.pre[root] = self.find(self.pre[root])
        return self.pre[root]

    def union(self, x, y):
        xroot = self.find(x)
        yroot = self.find(y)
        if xroot != yroot:
            self.pre[x] = yroot
            self.pre[xroot] = yroot

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = DSU(n)
        for edge in edges:
            graph.union(edge[0], edge[1])
        return len(set(graph.find(i) for i in range(n)))