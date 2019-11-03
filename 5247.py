class Solution:
    def minimumSwap(self, s1: str, s2: str) -> int:
        count1 = 0
        count2 = 0

        for i in range(len(s1)):
            if s1[i] == 'x' and s2[i] == 'y':
                count1 += 1
            if s1[i] == 'y' and s2[i] == 'x':
                count2 += 1

        if count1 % 2 + count2 % 2 == 1: return -1
        res = count1 // 2 + count2 // 2
        if count1 % 2 == 1 or count2 % 2 == 1:
            res += 2
        return res