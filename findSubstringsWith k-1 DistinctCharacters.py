class Solution:
    def subStringK1Characters(self, s, k):
        res = 0
        for left in range(len(s) - k + 1):
            right = left + k - 1
            visited = [0] * 27
            count = 0
            for i in range(left, right + 1):
                if visited[ord(s[i]) - 97] == 0:
                    count += 1
                visited[ord(s[i]) - 97] += 1
            if count == k - 1:
                res += 1
        return res

if __name__ == '__main__':
    solution = Solution()
    res = solution.subStringK1Characters('abcdabcd', 5)
    print(res)