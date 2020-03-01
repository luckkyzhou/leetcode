class Solution(object):
    def findJudge(self, N, trust):
        """
        :type N: int
        :type trust: List[List[int]]
        :rtype: int
        """
        a = [0 for _ in range(N + 1)]
        b = [0 for _ in range(N + 1)]

        for num in trust:
            a[num[1]] += 1
            b[num[0]] += 1

        for i, num in enumerate(a):
            if i != 0 and num == N - 1:
                if b[i] == 0: return i
        return -1