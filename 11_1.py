class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left = 0
        right = len(height) - 1
        res = 0
        while left < right:
            area = min(height[left], height[right]) * (right - left)
            res = max(res, area)
            if height[left] > height[right]:
                right -= 1
            else:
                left += 1
        return res
