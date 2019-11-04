class Solution:
    pathMax = -2 ** 31
    def maximumMinimumPath(self, matrix):
        pathMin = 2 ** 31
        self.DFS(matrix, 0, 0, pathMin)
        return self.pathMax
    def DFS(self, matrix, i, j, pathMin):
        m = len(matrix)
        n = len(matrix[0])
        if i >= m or j >= n:
            return
        if i == m - 1 and j == n - 1:
            pathMin = min(pathMin, matrix[i][j])
            self.pathMax = max(self.pathMax, pathMin)
            return
        pathMin = min(pathMin, matrix[i][j])
        self.DFS(matrix, i + 1, j, pathMin)
        self.DFS(matrix, i, j + 1, pathMin)

if __name__ == '__main__':
    solution = Solution()
    res = solution.maximumMinimumPath([[8,4,7],[6,5,9]])
    print(res)