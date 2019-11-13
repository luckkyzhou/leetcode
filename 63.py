from typing import List
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        dp = [[0 for _ in range(n)] for _ in range(m)]
        if obstacleGrid[0][0] == 0:
            dp[0][0] = 1
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0: continue
                if obstacleGrid[i][j] == 1: continue
                else:
                    dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        return dp[-1][-1]

if __name__ == '__main__':
    solution = Solution()
    res = solution.uniquePathsWithObstacles([[0,0,0],[0,1,0],[0,0,0]])
    print(res)