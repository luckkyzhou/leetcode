class Solution(object):
    def validTree(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: bool
        """
        from collections import defaultdict
        graph = defaultdict(list)
        for x, y in edges:
            graph[x].append(y)
            graph[y].append(x)

        visited = set()
        def DFS(i, prev):
            if i in visited: return False
            visited.add(i)
            for j in graph[i]:
                if j != prev and not DFS(j, i):
                    return False
            return True
        return DFS(0, None) and len(visited) == n