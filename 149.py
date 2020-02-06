from typing import List
from collections import Counter, defaultdict
class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        pointsDict = Counter(tuple(point) for point in points)
        onlyPoints = tuple(pointsDict.keys())
        n = len(onlyPoints)
        if n == 1: return pointsDict[onlyPoints[0]]

        def gcd(x, y):
            if y == 0: return x
            else: return gcd(y, x % y)

        res = 0
        for i in range(n - 1):
            x1, y1 = onlyPoints[i][0], onlyPoints[i][1]
            slope = defaultdict(int)
            for j in range(i + 1, n):
                x2, y2 = onlyPoints[j][0], onlyPoints[j][1]
                dx, dy = x2 - x1, y2 - y1
                g = gcd(dy, dx)
                if g != 0:
                    dx //= g
                    dy //= g
                slope[(dy, dx)] += pointsDict[onlyPoints[j]]
            res = max(res, max(slope.values()) + pointsDict[onlyPoints[i]])
        return res

if __name__ == '__main__':
    solution = Solution()
    res = solution.maxPoints([[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]])
    print(res)