class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """

        hash = set()
        res = 0
        left, right = 0, -1

        while left < len(s):
            while right + 1 < len(s) and s[right+1] not in hash:
                hash.add(s[right+1])
                right += 1
            res = max(res, right-left+1)
            left += 1
            hash.remove(s[left - 1])
        return res
