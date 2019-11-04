class Solution:
    def countkDist (self, str1, k):
        res = 0
        for i in range(0, len(str1)):
            count = 0
            amap = [0] * 27
            for j in range(i, len(str1)):
                if amap[ord(str1[j]) - 97] == 0:
                    count += 1
                amap[ord(str1[j]) - 97] += 1
                if count == k:
                    res += 1
                elif count > k:
                    break
        return res
if __name__ == '__main__':
    solution = Solution()
    res = solution.countkDist("abcbaa", 3)
    print(res)