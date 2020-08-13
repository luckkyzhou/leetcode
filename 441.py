class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 0
        left = 0
        right = n
        while left <= right:
            mid = left + (right - left) // 2
            coins = mid * (mid + 1) // 2
            if coins < n:
                left = mid + 1
            elif coins > n:
                right = mid - 1
            elif coins == n:
                return mid
        return left - 1
