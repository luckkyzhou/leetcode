class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        if s == "": return 0
        left = 0
        hashmap = {}
        count = 0
        maxLen = 1

        for right in range(len(s)):
            hashmap[s[right]] = hashmap.get(s[right], 0) + 1
            if hashmap[s[right]] == 1: count += 1
            if count <= 2:
                maxLen = max(maxLen, right - left + 1)
            while count > 2 and left < right:
                hashmap[s[left]] -= 1
                if hashmap[s[left]] == 0: count -=1
                left += 1
        return maxLen