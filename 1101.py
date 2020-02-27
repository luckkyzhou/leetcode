class DSU(object):
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

class Solution(object):
    def earliestAcq(self, logs, N):
        """
        :type logs: List[List[int]]
        :type N: int
        :rtype: int
        """
        dsu = DSU(N)

        logs.sort(key=lambda x:x[0])
        for log in logs:
            x, y = dsu.find(log[1]), dsu.find(log[2])
            if x == y: continue
            else:
                dsu.union(log[1], log[2])
                N -= 1
                if N == 1: return log[0]
        return -1