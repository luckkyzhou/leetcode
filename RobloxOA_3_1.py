class Solution:
    res = 0
    def palindrome(self, s):
        for i in range(len(s)):
            self.count(s, i, i)
            self.count(s, i, i + 1)
        return self.res

    def count(self, s: str, start: int, end: int):
        while start >= 0 and end < len(s) and s[start] == s[end]:
            self.res += 1
            start -= 1
            end += 1

if __name__ == '__main__':
    solution = Solution()
    res = solution.palindrome('aa')
    print(res)