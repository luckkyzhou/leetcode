# -*- coding: utf-8 -*-

from collections import deque

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s is None: return 0
        left = 0
        cur_len = 0
        max_len = 0
        queue = deque()

        for i in range(len(s)):
            cur_len += 1
            while s[i] in queue:
                queue.popleft()
                left += 1
                cur_len -= 1
            if cur_len > max_len: max_len = cur_len
            queue.append(s[i])
        return max_len