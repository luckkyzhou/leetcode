from typing import List

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)
        if k >= n - 1: return n

        hashmap = {}
        left, right = 0, 0
        res = 1
        curMax = 0
        while right < n:
            if s[right] not in hashmap:
                hashmap[s[right]] = 1
            else:
                hashmap[s[right]] += 1
            curMax = max(curMax, hashmap[s[right]])
            if right - left + 1 > curMax + k:
                hashmap[s[left]] -= 1
                left += 1
            res = max(res, right - left + 1)
            right += 1
        return res