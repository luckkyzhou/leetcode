class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        hashmap = {}
        left = 0
        n = len(s)
        count = 0
        res = 1

        if n == 0 or k == 0: return 0
        for right in range(n):
            if s[right] not in hashmap or hashmap[s[right]] == 0:
                hashmap[s[right]] = 1
                count += 1
            else:
                hashmap[s[right]] += 1
            if count <= k:
                res = max(res, right - left + 1)
            while count > k:
                if hashmap[s[left]] == 1:
                    count -= 1
                hashmap[s[left]] -= 1
                left += 1
        return res
if __name__ == '__main__':
    solution = Solution()
    res = solution.lengthOfLongestSubstringKDistinct("abaccc", 2)
    print(res)