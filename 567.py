import collections
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        m = len(s1)
        n = len(s2)
        dict_1 = dict(collections.Counter(s1))
        for left in range(n - m + 1):
            dict_2 = dict(collections.Counter(s2[left:left + m]))
            if dict_1 == dict_2:
                return True
        return False

if __name__ == '__main__':
    solution = Solution()
    res = solution.checkInclusion("adc", "dcda")
    print(res)