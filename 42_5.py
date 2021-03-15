class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left = 0
        left_max = [0 for _ in range(len(height))]
        right = 0
        right_max = [0 for _ in range(len(height))]

        res = 0

        for i in range(0, len(height)):
            left_max[i] = left
            left = max(left, height[i])
        for j in range(len(height)-1,-1,-1):
            right_max[j] = right
            right = max(right, height[j])
        for x in range(0, len(height)):
            if min(left_max[x], right_max[x]) > height[x]:
                res += min(left_max[x], right_max[x]) - height[x]
        return res
