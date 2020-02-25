class Solution(object):
    def getModifiedArray (self, length, updates):
        """
        :type length: int
        :type updates: List[List[int]]
        :rtype: List[int]
        """
        res = [0 for _ in range(length)]
        for i, j, num in updates:
            res[i] += num
            if j + 1 < length:
                res[j+1] -= num
        for i in range(1, length):
            res[i] = res[i] + res[i - 1]
        return res