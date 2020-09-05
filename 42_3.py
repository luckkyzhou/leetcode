class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left_height = []
        right_height = []
        left = 0
        right = 0
        res = 0
        for i in range(0, len(height)):
            left_height.append(left)
            left = max(left, height[i])
        for i in range(len(height)-1,-1,-1):
            right_height.append(right)
            right = max(right, height[i])
        right_height.reverse()
        for i in range(0, len(height)):
            min_height = min(left_height[i], right_height[i])
            if min_height > height[i]:
                res += min_height - height[i]
        return res
