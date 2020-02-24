class Solution(object):
    def findPermutation(self, s):
        """
        :type s: str
        :rtype: List[int]
        """
        res = [i for i in range(1, len(s) + 2)]
        for i in range(len(s) + 1):
            if s[i] == "I": continue
            start = i
            while i < len(s) + 1 and s[i] == "D": i += 1
            res[start:i+1] = res[start:i+1][::-1]
        return res