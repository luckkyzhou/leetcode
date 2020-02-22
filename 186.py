class Solution(object):
    def reverseWords(self, s):
        def reverse(s, i, j):
            left, right = i, j - 1
            while left < right:
                s[left], s[right] = s[right], s[left]
                left += 1
                right -= 1

        i = 0
        for j in range(len(s)):
            if s[j] != " ": continue
            reverse(s, i, j)
            i = j + 1
        reverse(s, i, len(s))
        reverse(s, 0, len(s))