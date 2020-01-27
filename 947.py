from typing import List
class DSU:
    def __init__(self, N):
        self.pre = [i for i in range(N)]

    def find(self, root):
        if self.pre[root] != root: self.pre[root] = self.find(self.pre[root])
        return self.pre[root]

    def union(self, x, y):
        xroot = self.find(x)
        yroot = self.find(y)
        if xroot != yroot:
            self.pre[x] = yroot
            self.pre[xroot] = yroot

class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        N = len(stones)
        dsu = DSU(20000)
        for x, y in stones: dsu.union(x, y + 10000)

        return N - len(set(dsu.find(x) for x, y in stones))

if __name__ == '__main__':
    solution = Solution()
    print(solution.removeStones([[0,0],[0,1],[1,0],[1,2],[2,1],[2,2]]))