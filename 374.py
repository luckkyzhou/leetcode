def guess(num):
    pass

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        left = 1
        right = n
        while left <= right:
            mid = left + (right - left) // 2
            if guess(mid) == -1:
                right = mid - 1
            elif guess(mid) == 1:
                left = mid + 1
            elif guess(mid) == 0:
                return mid