class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        n = len(heights)
        left = [0] * n
        right = [n] * n

        stack = []
        for i in range(0, n):
            while stack and heights[i] <= heights[stack[-1]]:
                right_edge = stack.pop()
                right[right_edge] = i
            left[i] = stack[-1] if stack else -1
            stack.append(i)

        res = 0
        for i in range(0, n):
            res = max(res, (right[i] - left[i] - 1) * heights[i])
        return res