class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num == 1: 
            return True
        
        left = 1
        right = num
        while left < right:
            mid = left + (right - left) // 2
            if mid * mid < num:
                left = mid + 1
            elif mid * mid > num:
                right = mid
            elif mid * mid == num:
                return True
        return False
