class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        visited1 = [0] * 27
        visited2 = [0] * 27
        if len(s1) > len(s2):
            return False

        for i in range(len(s1)):
            visited1[ord(s1[i]) - 97] += 1
            visited2[ord(s2[i]) - 97] += 1

        for left in range(0, len(s2) - len(s1) + 1):
            if visited1 == visited2:
                return True
            if left + len(s1) >= len(s2): break
            visited2[ord(s2[left]) - 97] -= 1
            visited2[ord(s2[left + len(s1)]) - 97] += 1

        return False

if __name__ == '__main__':
    solution = Solution()
    res = solution.checkInclusion("adc", "dcda")
    print(res)