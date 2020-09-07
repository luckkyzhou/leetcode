class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        n = len(heights)
        left = [0] * n
        right = [0] * n
        stack = []

        for i in range(0, n):
            while stack and heights[i] <= heights[stack[-1]]:
                stack.pop()
            left[i] = stack[-1] if stack else -1
            stack.append(i)

        stack = []
        for j in range(n-1,-1,-1):
            while stack and heights[j] <= heights[stack[-1]]:
                stack.pop()
            right[j] = stack[-1] if stack else n
            stack.append(j)

        res = 0
        for i in range(0, n):
            res = max(res, (right[i]-left[i]-1)*heights[i])
        return res