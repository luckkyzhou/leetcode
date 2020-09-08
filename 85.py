class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix: return 0

        def maxHistogram(heights):
            left = [0] * len(heights)
            right = [len(heights)] * len(heights)
            stack = []
            for i in range(len(heights)):
                while stack and heights[i] <= heights[stack[-1]]:
                    right_idx = stack.pop()
                    right[right_idx] = i
                left[i] = stack[-1] if stack else -1
                stack.append(i)
            maxArea = 0
            for i in range(len(heights)):
                maxArea = max(maxArea, (right[i] - left[i] - 1) * heights[i])
            return maxArea

        m = len(matrix)
        n = len(matrix[0])
        dp = [[0 for _ in range(n)] for _ in range(m)]

        res = 0
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == '1':
                    dp[i][j] = dp[i][j - 1] + 1
        for j in range(n):
            height = []
            for i in range(m):
                height.append(dp[i][j])
            res = max(res, maxHistogram(height))
        return res