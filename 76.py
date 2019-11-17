from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        left, right = 0, 0
        hashmap = {}
        dict_t = dict(Counter(t))
        tLength = len(dict_t)
        sLength = 0
        count = 2 ** 31
        while right < len(s):
            hashmap[s[right]] = hashmap.get(s[right], 0) + 1
            if s[right] in dict_t and hashmap[s[right]] == dict_t[s[right]]:
                sLength += 1
            while left <= right and sLength == tLength:
                if right - left + 1 < count:
                    res = s[left:right + 1]
                    count = right - left + 1
                hashmap[s[left]] -= 1
                if s[left] in dict_t and hashmap[s[left]] < dict_t[s[left]]:
                    sLength -= 1
                left += 1
            right += 1
        if count == 2 ** 31: return ""
        else: return res

if __name__ == '__main__':
    solution = Solution()
    res = solution.minWindow("ADOBECODEBANC","ABC")